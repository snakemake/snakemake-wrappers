"""Snakemake script for MSISensor msi"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import os
from os.path import commonprefix

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Extra parameters default value is an empty string
extra = snakemake.params.get("extra", "")

# Detemining common prefix in output files
# to fill the requested parameter '-o'
prefix = commonprefix(snakemake.output)

os.system(
    f"msisensor msi"  # Tool and its sub-command
    f" -d {snakemake.input.microsat}"  # Path to homopolymer/microsat file
    f" -n {snakemake.input.normal}"  # Path to normal bam
    f" -t {snakemake.input.tumor}"  # Path to tumor bam
    f" -o {prefix}"  # Path to output distribution file
    f" -b {snakemake.threads}"  # Maximum number of threads used
    f" {extra}"  # Optional extra parameters
    f" {log}"  # Logging behavior
)
