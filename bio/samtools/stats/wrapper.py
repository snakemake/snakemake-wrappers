"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts


bed = snakemake.input.get("bed", "")
if bed:
    bed = f"-t {bed}"

samtools_opts = get_samtools_opts(
    snakemake, parse_write_index=False, parse_output=False, parse_output_format=False
)


extra = snakemake.params.get("extra", "")
region = snakemake.params.get("region", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


shell(
    "samtools stats {samtools_opts} {extra} {snakemake.input[0]} {bed} {region} > {snakemake.output[0]} {log}"
)
