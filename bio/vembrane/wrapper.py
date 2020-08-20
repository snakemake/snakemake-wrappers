"""Snakemake wrapper for vembrane"""

__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2020, Christopher Schröder"
__email__ = "christopher.schroeder@tu-dortmund.de"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

os.system(
    f"vembrane"  # Tool and its subcommand
    f" {extra}"  # Extra parameters
    f' "{snakemake.params.expression}"'
    f" {snakemake.input.vcf}"  # Path to input vcf file
    f" > {snakemake.output.vcf}"  # Path to output vcf file
    f" {log}"  # Logging behaviour
)
