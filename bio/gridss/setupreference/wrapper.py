"""Snakemake wrapper for gridss setupreference"""

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

shell(
    "(gridss -s setupreference "  # Tool
    "--reference {snakemake.input.reference} "  # Reference
    "{extra}) {log}"
)
