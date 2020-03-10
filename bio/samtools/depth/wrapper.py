"""Snakemake wrapper for running samtools depth."""

__author__ = "Dayne L Filer"
__copyright__ = "Copyright 2020, Dayne L Filer"
__email__ = "dayne.filer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

# check for optional bed file
bed = "" if snakemake.input.bed == "" else "-b {}".format(snakemake.input.bed)

shell(
    "samtools depth {snakemake.params} {bed} "
    "-o {snakemake.output[0]} {snakemake.input.bams}"
)
