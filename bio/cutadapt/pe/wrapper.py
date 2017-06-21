"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


n = len(snakemake.input)
assert n == 2, "Input must contain 2 (paired-end) elements."

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "cutadapt"
    " {snakemake.params}"
    " -o {snakemake.output.fastq1}"
    " -p {snakemake.output.fastq2}"
    " {snakemake.input}"
    " > {snakemake.output.qc} {log}")
