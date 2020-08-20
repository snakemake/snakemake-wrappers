"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


import os

n = len(snakemake.input)
assert n == 2, "Input must contain 2 (paired-end) elements."

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    f"cutadapt"
    f" {snakemake.params.adapters}"
    f" {snakemake.params.others}"
    f" -o {snakemake.output.fastq1}"
    f" -p {snakemake.output.fastq2}"
    f" -j {snakemake.threads}"
    f" {snakemake.input}"
    f" > {snakemake.output.qc} {log}"
)
