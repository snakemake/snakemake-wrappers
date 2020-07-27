__author__ = "Christopher Schröder, Patrik Smeds"
__copyright__ = "Copyright 2020, Christopher Schröder, Patrik Smeds"
__email__ = "christopher.schroeder@tu-dortmund.de, patrik.smeds@gmail.com"
__license__ = "MIT"

from os import path

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Check inputs/arguments.
if len(snakemake.input) == 0:
    raise ValueError("A reference genome has to be provided.")
elif len(snakemake.input) > 1:
    raise ValueError("Please provide exactly one reference genome as input.")

# Prefix that should be used for the database
prefix = snakemake.params.get("prefix", "")

if len(prefix) > 0:
    prefix = "-p " + prefix

shell("bwa-mem2 index" " {prefix}" " {snakemake.input[0]}" " {log}")
