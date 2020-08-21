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

if not bam or (isinstance(bam, list) and len(bam) != 1):
    raise ValueError("Please provide exactly one 'bam' as input.")

if not path.exists(bam + ".bai"):
    raise ValueError(
        "Please index the bam file. The index file must have same file name as the bam file, with '.bai' appended."
    )

if not reference:
    raise ValueError("Please provide a fasta 'reference' input.")

if not bounds:  # optional
    bounds_string = ""
else:
    bounds_string = "-b {}".format(bounds)

if not path.exists(reference + ".fai"):
    raise ValueError(
        "Please index the reference. The index file must have same file name as the reference file, with '.fai' appended."
    )

if not any(o.endswith("-bounds.txt") for o in snakemake.output):
    raise ValueError("Please provide a file that ends with -bounds.txt in the output.")

for filename in snakemake.output:
    if filename.endswith("-bounds.txt"):
        prefix = filename[: -len("-bounds.txt")]
        break

if not any(o == "{}-genotype.txt".format(prefix) for o in snakemake.output):
    raise ValueError(
        "Please provide an output file that ends with -genotype.txt and has the same prefix as -bounds.txt"
    )

if not any(o == "{}-unplaced.txt".format(prefix) for o in snakemake.output):
    raise ValueError(
        "Please provide an output file that ends with -unplaced.txt and has the same prefix as -bounds.txt"
    )

shell(
    "(strling call "
    "{bam} "
    "{bin} "
    "{bounds_string} "
    "-o {prefix} "
    "{extra}) {log}"
)
