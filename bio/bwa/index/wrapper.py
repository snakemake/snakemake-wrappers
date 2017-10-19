__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2016, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from os import path

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

#Check inputs/arguments.
if len(snakemake.input) == 0:
    raise ValueError("A reference genome has to be provided!")
elif len(snakemake.input) > 1:
    raise ValueError("Only one reference genome can be inputed!")

#Prefix that should be used with for the database
prefix = snakemake.params.get("prefix", "")

if len(prefix) > 0:
    prefix = "-p " + prefix

#Contrunction algorithm that will be used to build the database, default is bwtsw
construction_algorithm = snakemake.params.get("algorithm", "bwtsw")

shell(
    "bwa index"
    " {prefix}"
    " -a {construction_algorithm}"
    " {snakemake.input[0]}"
    " {log}")

