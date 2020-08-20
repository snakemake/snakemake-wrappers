"""Snakemake wrapper for strling call"""

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
bin = snakemake.input.get("bin", None)
reference = snakemake.input.get("reference", None)
bounds = snakemake.input.get("bounds", None)
prefix = snakemake.params.get("prefix", None)

if not bam:
    raise ValueError("Please provide exactly one 'bam' as input.")

if not path.exists(bam + ".bai"):
    raise ValueError("Please index the bam and generate the .bam.bai file")

if not reference:
    raise ValueError("Please provide a fasta 'reference' input.")

if not bounds: # optional
    bounds_string = ""
else:
    bounds_string = f"-b {bounds}"

if not path.exists(reference + ".fai"):
    raise ValueError("Please index the reference and generate the *.bai file")

shell(
    "(strling call "
    "{bam} "
    "{bin} "
    "{bounds_string} "
    "-o {prefix} "
    "{extra}) {log}"
)
