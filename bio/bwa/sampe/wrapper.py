"""Snakemake wrapper for bwa sampe."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from os import path

from snakemake.shell import shell

index = snakemake.input.get("idx", "")
if isinstance(index, str):
    index = path.splitext(snakemake.input.idx)[0]
else:
    index = path.splitext(snakemake.input.idx[0])[0]

# Check inputs.
if not len(snakemake.input.sai) == 2:
    raise ValueError("input.sai must have 2 elements")

if not len(snakemake.input.fastq) == 2:
    raise ValueError("input.fastq must have 2 elements")

# Extract arguments.
extra = snakemake.params.get("extra", "")

sort = snakemake.params.get("sort", "none")
sort_order = snakemake.params.get("sort_order", "coordinate")
sort_extra = snakemake.params.get("sort_extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Determine which pipe command to use for converting to bam or sorting.
if sort == "none":
    # Simply convert to bam using samtools view.
    pipe_cmd = "samtools view -Sbh -o {snakemake.output[0]} -"

elif sort == "samtools":
    # Sort alignments using samtools sort.
    pipe_cmd = "samtools sort {sort_extra} -o {snakemake.output[0]} -"

    # Add name flag if needed.
    if sort_order == "queryname":
        sort_extra += " -n"

    # Use prefix for temp.
    prefix = path.splitext(snakemake.output[0])[0]
    sort_extra += " -T " + prefix + ".tmp"

elif sort == "picard":
    # Sort alignments using picard SortSam.
    pipe_cmd = (
        "picard SortSam {sort_extra} INPUT=/dev/stdin"
        " OUTPUT={snakemake.output[0]} SORT_ORDER={sort_order}"
    )

else:
    raise ValueError("Unexpected value for params.sort ({})".format(sort))

# Run command.
shell(
    "(bwa sampe"
    " {extra}"
    " {index}"
    " {snakemake.input.sai}"
    " {snakemake.input.fastq}"
    " | " + pipe_cmd + ") {log}"
)
