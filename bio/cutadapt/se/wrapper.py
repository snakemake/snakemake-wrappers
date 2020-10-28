"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


n = len(snakemake.input)
assert n == 1, "Input must contain 1 (single-end) elements."

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "cutadapt"
    " {snakemake.params.adapters}"
    " {snakemake.params.extra}"
    " -j {snakemake.threads}"
    " -o {snakemake.output.fastq}"
    " {snakemake.input[0]}"
    " > {snakemake.output.qc} {log}"
)
