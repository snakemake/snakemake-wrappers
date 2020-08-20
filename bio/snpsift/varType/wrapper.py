"""Snakemake wrapper for SnpSift varType"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

os.system(
    f"SnpSift varType"  # Tool and its subcommand
    f" {extra}"  # Extra parameters
    f" {snakemake.input.vcf}"  # Path to input vcf file
    f" > {snakemake.output.vcf}"  # Path to output vcf file
    f" {log}"  # Logging behaviour
)
