"""Snakemake wrapper for strling index"""

__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2020, Christopher Schröder"
__email__ = "christopher.schroede@tu-dortmund.de"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

# Creating log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")

# Check inputs/arguments.
if len(snakemake.input) != 1:
    raise ValueError("Please provide exactly one reference genome.")

shell(
    "(strling index {snakemake.input[0]} "
    "-g {snakemake.output.index} "
    "{extra}) {log}"
)
