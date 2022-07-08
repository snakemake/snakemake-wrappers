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
# all output files have a single file extension, except bwat.2bit.64
if snakemake.output[0].endswith(".bwt.2bit.64"):
    prefix = snakemake.output[0][0 : -len(".bwt.2bit.64")]
else:
    prefix, _ = path.splitext(snakemake.output[0])

shell(f"bwa-mem2 index -p {prefix} {snakemake.input[0]} {log}")
