__author__ = "Johannes Köster, Julian de Ruiter"
__copyright__ = "Copyright 2016, Johannes Köster and Julian de Ruiter"
__email__ = "koester@jimmy.harvard.edu, julianderuiter@gmail.com"
__license__ = "MIT"

import errno
import os

from snakemake.shell import shell


n = len(snakemake.input)
assert n == 1 or n == 2, "Input must have 1 (single-end) or 2 (paired-end) elements."

extra = snakemake.params.get('extra', '')

sort = snakemake.params.get('sort', 'none')
sort_order = snakemake.params.get('sort_order', 'coordinate')
sort_extra = snakemake.params.get('sort_extra', '')

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

if sort == 'none':

    # Run bwa mem, piped into samtools view.
    shell(
        "(bwa mem"
        " -t {snakemake.threads}"
        " {extra}"
        " {snakemake.params.index}"
        " {snakemake.input} |"
        " samtools view -Sbh -o {snakemake.output[0]} -"
        ") {log}")

elif sort == 'samtools':

    # Create output directory if it doesn't exist.
    output_dir = os.path.dirname(snakemake.output[0])

    try:
        os.makedirs(output_dir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    # Add name flag if needed.
    if sort_order == 'queryname':
        sort_extra += ' -n'

    # Run bwa mem, piped into samtools sort. Temp prefix
    # is needed to avoid issue with samtools not being
    # able to open the output files.
    temp_prefix = os.path.splitext(snakemake.output[0])[0]

    shell(
        "(bwa mem"
        " -t {snakemake.threads}"
        " {extra}"
        " {snakemake.params.index}"
        " {snakemake.input} |"
        " samtools sort"
        " {sort_extra}"
        " -o {snakemake.output[0]}"
        " -T {temp_prefix}"
        " -"
        ") {log}")

elif sort == 'picard':

    # Run bwa mem, piped into picard SortSam.
    shell(
        "(bwa mem"
        " -t {snakemake.threads}"
        " {extra}"
        " {snakemake.params.index}"
        " {snakemake.input} |"
        " picard SortSam"
        " {sort_extra}"
        " INPUT=/dev/stdin"
        " OUTPUT={snakemake.output[0]}"
        " SORT_ORDER={sort_order}"
        ") {log}")

else:
    raise ValueError('Unknown value for params.sort ({})'.format(sort))
