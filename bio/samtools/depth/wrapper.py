"""Snakemake wrapper for running samtools depth."""

__author__ = "Dayne L Filer"
__copyright__ = "Copyright 2020, Dayne L Filer"
__email__ = "dayne.filer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

params = snakemake.params.get("extra", "")

# check for optional bed file
bed = snakemake.input.get("bed", "")
if bed:
    bed = "-b " + bed

shell(
    "samtools depth {params} {bed} " "-o {snakemake.output[0]} {snakemake.input.bams}"
)
