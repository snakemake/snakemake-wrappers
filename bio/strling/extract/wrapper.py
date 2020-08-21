"""Snakemake wrapper for strling extract"""

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
bam = snakemake.input.get("bam", None)
reference = snakemake.input.get("reference", None)
index = snakemake.input.get("index", None)

if not bam or (isinstance(bam, list) and len(bam) != 1):
    raise ValueError("Please provide exactly one 'bam' input.")

if not path.exists(bam + ".bai"):
    raise ValueError(
        "Please index the bam file. The index file must have same file name as the bam file, with '.bai' appended."
    )

if not reference:
    raise ValueError("Please provide a fasta 'reference' input.")

if not path.exists(reference + ".fai"):
    raise ValueError(
        "Please index the reference. The index file must have same file name as the reference file, with '.fai' appended."
    )

if not index:  # optional
    index_string = ""
else:
    index_string = "-g {}".format(index)

if len(snakemake.output) != 1:
    raise ValueError("Please provide exactly one output file (.bin).")

shell(
    "(strling extract "
    "{bam} "
    "{snakemake.output[0]} "
    "-f {reference} "
    "{index_string} "
    "{extra}) {log}"
)
