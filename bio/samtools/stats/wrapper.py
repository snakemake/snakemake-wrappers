"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

bed = snakemake.params.get("bed", None)
if bed is not None:
    bed = " -t " + bed

extra = snakemake.params.get("extra", "")
region = snakemake.params.get("region", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


shell(
    "samtools stats {extra} {snakemake.input} {bed} {region} > {snakemake.output} {log}"
)
