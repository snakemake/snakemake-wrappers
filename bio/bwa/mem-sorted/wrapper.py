"""Snakemake wrapper for aligning reads using bwa mem and sorting the
alignments using  picard SortSam."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

sort_order = snakemake.params.get('sort_order', 'coordinate')
log = snakemake.log_fmt_shell(stderr=True)

shell(
    '(bwa mem'
    ' -t {snakemake.threads}'
    ' {snakemake.params.bwa_extra}'
    ' {snakemake.input.ref}'
    ' {snakemake.input.sample} |'
    ' picard SortSam'
    ' {snakemake.params.sort_extra}'
    ' INPUT=/dev/stdin'
    ' OUTPUT={snakemake.output[0]}'
    ' SORT_ORDER={sort_order}'
    ') {log}')
