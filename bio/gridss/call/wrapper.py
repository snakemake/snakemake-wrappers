"""Snakemake wrapper for gridss call"""

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
if not snakemake.params.workingdir:
    raise ValueError("Please set params.workingdir to provide a working directory.")

if not snakemake.input.reference:
    raise ValueError("Please set input.reference to provide reference genome.")

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
    "(export JAVA_OPTS='-XX:ActiveProcessorCount={snakemake.threads}' & "
    "gridss -s call "  # Tool
    "--reference {reference} "  # Reference
    "--threads {snakemake.threads} "  # Threads
    "--workingdir {snakemake.params.workingdir} "  # Working directory
    "--assembly {snakemake.input.assembly} "  # Assembly input from gridss assemble
    "--output {snakemake.output.vcf} "  # Assembly vcf
    "{snakemake.input.bams} "
    "{extra}) {log}"
)
