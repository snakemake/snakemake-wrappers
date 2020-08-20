"""Snakemake wrapper for bwa aln."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


import os


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    f"bwa aln"
    f" {extra}"
    f" -t {snakemake.threads}"
    f" {snakemake.params.index}"
    f" {snakemake.input[0]}"
    f" > {snakemake.output[0]} {log}"
)
