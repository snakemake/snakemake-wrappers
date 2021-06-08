__author__ = "Johannes Köster, Julian de Ruiter"
__copyright__ = "Copyright 2016, Johannes Köster and Julian de Ruiter"
__email__ = "koester@jimmy.harvard.edu, julianderuiter@gmail.com"
__license__ = "MIT"


from os import path
import re
import tempfile
from snakemake.shell import shell


# Extract arguments.
extra = snakemake.params.get("extra", "")

sort = snakemake.params.get("sorting", "none")
sort_order = snakemake.params.get("sort_order", "coordinate")
sort_extra = snakemake.params.get("sort_extra", "")

if re.search(r"-T\b", sort_extra) or re.search(r"--TMP_DIR\b", sort_extra):
    sys.exit(
        "You have specified temp dir (`-T` or `--TMP_DIR`) in params.sort_extra; this is automatically set from params.tmp_dir."
    )

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

tmp_dir = snakemake.params.get("tmp_dir")
if tmp_dir:
    tempfile.tempdir = tmp_dir


# Check inputs/arguments.
if not isinstance(snakemake.input.reads, str) and len(snakemake.input.reads) not in {
    1,
    2,
}:
    raise ValueError("input must have 1 (single-end) or " "2 (paired-end) elements")

if sort_order not in {"coordinate", "queryname"}:
    raise ValueError("Unexpected value for sort_order ({})".format(sort_order))

# Determine which pipe command to use for converting to bam or sorting.
if sort == "none":

    # Simply convert to bam using samtools view.
    pipe_cmd = "samtools view -Sbh -o {snakemake.output[0]} -"

elif sort == "samtools":

    # Add name flag if needed.
    if sort_order == "queryname":
        sort_extra += " -n"

    # Sort alignments using samtools sort.
    pipe_cmd = "samtools sort -T {tmp} {sort_extra} -o {snakemake.output[0]} -"

elif sort == "picard":

    # Sort alignments using picard SortSam.
    pipe_cmd = (
        "picard SortSam {sort_extra} --INPUT /dev/stdin"
        " --OUTPUT {snakemake.output[0]} --SORT_ORDER {sort_order} --TMP_DIR {tmp}"
    )

else:
    raise ValueError("Unexpected value for params.sort ({})".format(sort))

with tempfile.TemporaryDirectory() as tmp:
    shell(
        "(bwa mem"
        " -t {snakemake.threads}"
        " {extra}"
        " {snakemake.params.index}"
        " {snakemake.input.reads}"
        " | " + pipe_cmd + ") {log}"
    )
