"""Snakemake wrapper for picard SortSam."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    'picard'
    ' SortSam'
    ' {extra}'
    ' INPUT={snakemake.input[0]}'
    ' OUTPUT={snakemake.output[0]}'
    ' SORT_ORDER={snakemake.params.sort_order}'
    ' {log}')
