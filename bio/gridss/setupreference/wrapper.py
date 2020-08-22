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
reference = snakemake.input.get("reference", None)

if not snakemake.input.reference:
    raise ValueError("A reference genome has to be provided!")

for ending in (".amb", ".ann", ".bwt", ".pac", ".sa"):
    if not path.exists("{}{}".format(reference, ending)):
        raise ValueError(
            "{reference}{ending} missing. Please make sure the reference was properly indexed by bwa.".format(
                reference=reference, ending=ending
            )
        )

dictionary = path.splitext(reference)[0] + ".dict"
if not path.exists(dictionary):
    raise ValueError(
        "{dictionary}.dict missing. Please make sure the reference dictionary was properly created. This can be accomplished for example by CreateSequenceDictionary.jar from Picard".format(
            dictionary=dictionary
        )
    )

shell(
    "(gridss -s setupreference "  # Tool
    "--reference {reference} "  # Reference
    "{extra}) {log}"
)
