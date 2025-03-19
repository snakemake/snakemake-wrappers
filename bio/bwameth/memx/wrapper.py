# coding: utf-8

"""
Snakemake wrapper for bwameth

Proceeed according to other bwa wrappers: Align + optional sort
"""
__author__ = "Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__copyright__ = "Copyright 2024, Thibault Dayris"
__license__ = "MIT"

import os.path
import time

from tempfile import TemporaryDirectory
from snakemake import shell
from snakemake_wrapper_utils.java import get_java_opts
from snakemake_wrapper_utils.samtools import get_samtools_opts

# Extract arguments
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True, append=True)

sort = snakemake.params.get("sort", "none")
sort_order = snakemake.params.get("sort_order", "coordinate")
sort_extra = snakemake.params.get("sort_extra", "")
samtools_opts = get_samtools_opts(snakemake, param_name="sort_extra")
java_opts = get_java_opts(snakemake)

bwa_threads = snakemake.threads
samtools_threads = snakemake.threads - 1

# Checking required indexes
mem_idx = {
    ".c2t",
    ".c2t.amb",
    ".c2t.ann",
    ".c2t.bwt",
    ".c2t.pac",
    ".c2t.sa",
}

mem2_idx = {
    ".c2t",
    ".c2t.0123",
    ".c2t.amb",
    ".c2t.ann",
    ".c2t.bwt.2bit.64",
    ".c2t.pac",
}

# Extract index prefix, and list of index extensions
index = os.path.commonprefix(snakemake.input.idx)
index_extensions = set(idx[len(index) - 4 :] for idx in snakemake.input.idx)
missing_mem_idx = mem_idx - index_extensions
missing_mem2_idx = mem2_idx - index_extensions
if (len(missing_mem2_idx) > 0) and (len(missing_mem_idx) > 0):
    # If ONE of the sets is empty, then all the index for one of the aligners
    # are present.
    raise ValueError(
        "Missing required indices for both bwa-mem and bwa-mem2. No aligner can "
        f"be launched. bwa-mem misses {missing_mem_idx}, while bwa-mem2 misses "
        f"{missing_mem2_idx}. Please provide missing files. {index_extensions}"
    )


# Check arguments
if sort_order not in {"coordinate", "queryname"}:
    raise ValueError(f"Unexpected value for sort_order ({sort_order})")

# Determine which pipe command to use for converting to bam or sorting.
if sort == "none":
    # Correctly assign number of threads according to user request
    if samtools_threads >= 1:
        samtools_opts += " --threads {samtools_threads} "

    if str(snakemake.output[0]).lower().endswith(("bam", "cram")):
        # Simply convert to bam using samtools view.
        pipe_cmd = " | samtools view {samtools_opts} > {snakemake.output[0]}"
    else:
        # Do not perform any sort nor compression, output raw sam
        pipe_cmd = " > {snakemake.output[0]} "


elif sort == "samtools":
    # Correctly assign number of threads according to user request
    if samtools_threads >= 1:
        samtools_opts += " --threads {samtools_threads} "

    # Add name flag if needed.
    if sort_order == "queryname":
        sort_extra += " -n"

    # Sort alignments using samtools sort.
    pipe_cmd = " | samtools sort {samtools_opts} {sort_extra} -T {tmpdir} > {snakemake.output[0]}"


elif sort == "picard":
    # Correctly assign number of threads according to user request
    bwa_threads -= 1
    if bwa_threads <= 0:
        raise ValueError(
            "Not enough threads requested. This wrapper requires exactly one more."
        )

    # Sort alignments using picard SortSam.
    pipe_cmd = (
        " | picard SortSam {java_opts} {sort_extra} "
        "--INPUT /dev/stdin "
        "--TMP_DIR {tmpdir} "
        "--SORT_ORDER {sort_order} "
        "--OUTPUT {snakemake.output[0]}"
    )


else:
    raise ValueError(f"Unexpected value for params.sort ({sort})")

# Gathering fastq files to align
fq = snakemake.input.get("fq")
fq1 = snakemake.input.get("fq1")
fq2 = snakemake.input.get("fq2")

# Single-ended case
if fq:
    if isinstance(fq, list):
        fastq_files = ",".join(fq)
    else:
        fastq_files = fq

# Pair-ended case
elif fq1 and fq2:
    if isinstance(fq1, list) and isinstance(fq2, list):
        if len(fq1) == len(fq2):
            fastq_files = f'{",".join(fq1)} {",".join(fq2)}'
        else:
            raise ValueError("Please provide as many R1 and R2 files")
    else:
        fastq_files = f"{fq1} {fq2}"

# Missing fastq case
else:
    raise ValueError("Either provide `input.fq` or both `input.fq1` and `input.fq2`")

with TemporaryDirectory() as tmpdir:
    shell(
        "(bwameth.py --threads {snakemake.threads} "
        " {extra} --reference {snakemake.input.ref} {fastq_files} "
        " {fastq_files} " + pipe_cmd + " ) {log}"
    )
