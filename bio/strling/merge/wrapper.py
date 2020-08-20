"""Snakemake wrapper for strling merge"""

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
bins = snakemake.input.get("bins")
reference = snakemake.input.get("reference")
fai = snakemake.input.get("fai")
prefix = snakemake.params.get("prefix")

if not bins or len(bins) < 2:
    raise ValueError("Please provide at least two 'bins' as input.")

if not reference:
    raise ValueError("Please provide a fasta 'reference' input.")

if not path.exists(reference + ".fai"):
    raise ValueError(
        "Please index the reference. The index file must have same file name as the reference file, with '.fai' appended."
    )

if len(snakemake.output) != 1:
    raise ValueError("Please provide exactly one output file (.bin).")

shell("(strling merge " "{bins} " "-o {prefix} " "{extra}) {log}")
