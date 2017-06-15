"""Snakemake wrapper for bwa sampe."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


if not len(snakemake.input.sai) == 2:
    raise ValueError('input.sai must have 2 elements')

if not len(snakemake.input.fastq) == 2:
    raise ValueError('input.fastq must have 2 elements')

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "(bwa sampe"
    " {snakemake.params.extra}"
    " {snakemake.params.index}"
    " {snakemake.input.sai}"
    " {snakemake.input.fastq}"
    " | samtools view -Sbh -o {snakemake.output[0]} -"
    ") {log}")
