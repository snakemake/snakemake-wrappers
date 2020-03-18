"""Snakemake wrapper for SnpSift varType"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

shell(
    "SnpSift varType"  # Tool and its subcommand
    " {extra}"  # Extra parameters
    " {snakemake.input.vcf}"  # Path to input vcf file
    " > {snakemake.output.vcf}"  # Path to output vcf file
    " {log}"  # Logging behaviour
)
