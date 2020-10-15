"""Snakemake wrapper for both bwa samse and sampe."""

__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"


from os import path

from snakemake.shell import shell


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

# Extract arguments.
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)


# Run command.
shell(
    "(bwa {alg}"
    " {extra}"
    " {snakemake.params.index}"
    " {snakemake.input.sai}"
    " {snakemake.input.fastq}"
    "> {snakemake.output[0]}) {log}"
)
