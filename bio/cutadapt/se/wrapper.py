"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


import os


log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    f"cutadapt"
    " {snakemake.params}"
    " -j {snakemake.threads}"
    " -o {snakemake.output.fastq}"
    " {snakemake.input[0]}"
    " > {snakemake.output.qc} {log}"
)
