"""Snakemake wrapper for shovill."""

__author__ = "Sangram Keshari Sahu"
__copyright__ = "Copyright 2020, Sangram Keshari Sahu"
__email__ = "sangramsahu15@gmail.com"
__license__ = "MIT"

import os
from os import path
from snakemake.shell import shell

# Placeholder for optional parameters
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
params = snakemake.params.get("extra", "")

shell(
    "(shovill"
    " --assembler {snakemake.params.assembler}"
    " --outdir assembly"
    " --R1 {snakemake.input.r1}"
    " --R2 {snakemake.input.r2}"
    " --cpus {snakemake.threads}"
    " {snakemake.params.extra}) {log}"
)

os.rename(
    "assembly/" + snakemake.params.assembler + ".fasta", "assembly/raw_assembly.fa"
)
