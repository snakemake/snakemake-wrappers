"""Snakemake wrapper for both bwa samse and sampe."""

__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2020, Filipe G. Vieira"
__license__ = "MIT"


from os import path

from snakemake.shell import shell


index = snakemake.input.get("idx", "")
if isinstance(index, str):
    index = path.splitext(snakemake.input.idx)[0]
else:
    index = path.splitext(snakemake.input.idx[0])[0]

# Check inputs.
fastq = (
    snakemake.input.fastq
    if isinstance(snakemake.input.fastq, list)
    else [snakemake.input.fastq]
)
sai = (
    snakemake.input.sai
    if isinstance(snakemake.input.sai, list)
    else [snakemake.input.sai]
)
if len(fastq) == 1 and len(sai) == 1:
    alg = "samse"
elif len(fastq) == 2 and len(sai) == 2:
    alg = "sampe"
else:
    raise ValueError("input.fastq and input.sai must have 1 or 2 elements each")

# Extract output format
out_name, out_ext = path.splitext(snakemake.output[0])
out_ext = out_ext[1:].upper()

# Extract arguments.
extra = snakemake.params.get("extra", "")

sort = snakemake.params.get("sort", "none")
sort_order = snakemake.params.get("sort_order", "coordinate")
sort_extra = snakemake.params.get("sort_extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Determine which pipe command to use for converting to bam or sorting.
if sort == "none":
    # Simply convert to output format using samtools view.
    pipe_cmd = (
        "samtools view -h --output-fmt " + out_ext + " -o {snakemake.output[0]} -"
    )

elif sort == "samtools":
    # Sort alignments using samtools sort.
    pipe_cmd = "samtools sort {sort_extra} -o {snakemake.output[0]} -"

    # Add name flag if needed.
    if sort_order == "queryname":
        sort_extra += " -n"

    # Use prefix for temp.
    prefix = path.splitext(snakemake.output[0])[0]
    sort_extra += " -T " + prefix + ".tmp"

    # Define output format
    sort_extra += " --output-fmt {}".format(out_ext)

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
    "(bwa {alg}"
    " {extra}"
    " {index}"
    " {snakemake.input.sai}"
    " {snakemake.input.fastq}"
    " | " + pipe_cmd + ") {log}"
)
