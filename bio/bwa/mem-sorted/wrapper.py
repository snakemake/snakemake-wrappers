"""Snakemake wrapper for aligning reads using bwa mem and sorting the
alignments using samtools."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"

import errno
import os

from snakemake.shell import shell


# Create output directory if it doesn't exist.
output_dir = os.path.dirname(snakemake.output[0])

try:
    os.makedirs(output_dir)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise

# Run command. Temp prefix is needed to avoid issue with
# samtools not being able to open the output files.
temp_prefix = os.path.splitext(snakemake.output[0])[0]
log = snakemake.log_fmt_shell(stderr=True)

shell(
    "(bwa mem"
    " -t {snakemake.threads}"
    " {snakemake.params.bwa_extra}"
    " {snakemake.input.ref}"
    " {snakemake.input.sample} |"
    " samtools sort"
    " {snakemake.params.sort_extra}"
    " -o {snakemake.output[0]}"
    " -T {temp_prefix}"
    " -"
    ") {log} ")
