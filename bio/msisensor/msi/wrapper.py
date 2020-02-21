"""Snakemake script for MSISensor msi"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from os.path import commonprefix
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Extra parameters default value is an empty string
extra = snakemake.params.get("extra", "")

# Detemining common prefix in output files
# to fill the requested parameter '-o'
prefix = commonprefix(snakemake.output)

shell(
    "msisensor msi"  # Tool and its sub-command
    " -d {snakemake.input.microsat}"  # Path to homopolymer/microsat file
    " -n {snakemake.input.normal}"  # Path to normal bam
    " -t {snakemake.input.tumor}"  # Path to tumor bam
    " -o {prefix}"  # Path to output distribution file
    " -b {snakemake.threads}"  # Maximum number of threads used
    " {extra}"  # Optional extra parameters
    " {log}"  # Logging behavior
)
