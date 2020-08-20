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
    " {extra}"
    " -t {snakemake.threads}"
    " {snakemake.params.index}"
    " {snakemake.input[0]}"
    " > {snakemake.output[0]} {log}"
)
