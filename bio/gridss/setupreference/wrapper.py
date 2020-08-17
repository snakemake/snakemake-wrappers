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

# Check inputs/arguments.
reference = snakemake.input.get("reference")
dictionary = snakemake.input.get("dictionary")
if not snakemake.input.reference:
    raise ValueError("A reference genome has to be provided!")

for ending in (".amb", ".ann", ".bwt", ".pac", ".sa"):
    if not path.exists(f"{reference}{ending}"):
        raise ValueError(
            f"{reference}{ending} missing. Please make sure the reference was properly indexed by bwa."
        )

if not path.exists(f"{dictionary}"):
    raise ValueError(
        f"{reference}{ending} missing. Please make sure the reference dictionary was properly created. This can be accomplished for example by CreateSequenceDictionary.jar from Picard"
    )

shell(
    "(gridss -s setupreference "  # Tool
    "--reference {reference} "  # Reference
    "{extra}) {log}"
)
