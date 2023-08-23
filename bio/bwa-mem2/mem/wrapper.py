__author__ = "Christopher Schröder, Johannes Köster, Julian de Ruiter"
__copyright__ = (
    "Copyright 2020, Christopher Schröder, Johannes Köster and Julian de Ruiter"
)
__email__ = "christopher.schroeder@tu-dortmund.de koester@jimmy.harvard.edu, julianderuiter@gmail.com"
__license__ = "MIT"


import tempfile
from os import path
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts
from snakemake_wrapper_utils.samtools import get_samtools_opts


# Extract arguments.
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
sort = snakemake.params.get("sort", "none")
sort_order = snakemake.params.get("sort_order", "coordinate")
sort_extra = snakemake.params.get("sort_extra", "")
samtools_opts = get_samtools_opts(
    snakemake, parse_threads=False, param_name="sort_extra"
)
java_opts = get_java_opts(snakemake)

bwa_threads = snakemake.threads
samtools_threads = snakemake.threads - 1

index = snakemake.input.get("index", "")
if isinstance(index, str):
    index = path.splitext(snakemake.input.idx)[0]
else:
    index = path.splitext(snakemake.input.idx[0])[0]


# Check inputs/arguments.
if not isinstance(snakemake.input.reads, str) and len(snakemake.input.reads) not in {
    1,
    2,
}:
    raise ValueError("input must have 1 (single-end) or 2 (paired-end) elements")

if sort_order not in {"coordinate", "queryname"}:
    raise ValueError(f"Unexpected value for sort_order ({sort_order})")

# Determine which pipe command to use for converting to bam or sorting.
if sort == "none":
    # Correctly assign number of threads according to user request
    if samtools_threads >= 1:
        samtools_opts += f" --threads {samtools_threads} "

    if str(snakemake.output[0]).lower().endswith(("bam", "cram")):
        # Simply convert to bam using samtools view.
        pipe_cmd = " | samtools view {samtools_opts} > {snakemake.output[0]}"
    else:
        # Do not perform any sort nor compression, output raw sam
        pipe_cmd = " > {snakemake.output[0]} "


elif sort == "samtools":
    # Correctly assign number of threads according to user request
    if samtools_threads >= 1:
        samtools_opts += f" --threads {samtools_threads} "

    # Add name flag if needed.
    if sort_order == "queryname":
        sort_extra += " -n"

    # Sort alignments using samtools sort.
    pipe_cmd = " | samtools sort {samtools_opts} {sort_extra} -T {tmpdir} > {snakemake.output[0]}"

elif sort == "picard":
    # Correctly assign number of threads according to user request
    bwa_threads = bwa_threads - 1
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

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(bwa-mem2 mem"
        " -t {bwa_threads}"
        " {extra}"
        " {index}"
        " {snakemake.input.reads}"
        " " + pipe_cmd + " ) {log}"
    )
