"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


import os


log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    f"cutadapt"
    f" {snakemake.params}"
    f" -j {snakemake.threads}"
    f" -o {snakemake.output.fastq}"
    f" {snakemake.input[0]}"
    f" > {snakemake.output.qc} {log}"
)
