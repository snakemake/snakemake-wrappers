"""Snakemake wrapper for bwa aln."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

index = snakemake.input.idx
if isinstance(index, str):
    index = path.splitext(snakemake.input.idx)[0]
else:
    index = path.splitext(snakemake.input.idx[0])[0]

shell(
    "bwa aln"
    " {extra}"
    " -t {snakemake.threads}"
    " {index}"
    " {snakemake.input.fastq}"
    " > {snakemake.output[0]} {log}"
)
