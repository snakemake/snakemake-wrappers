"""Snakemake wrapper for shovill."""

__author__ = "Sangram Keshari Sahu"
__copyright__ = "Copyright 2020, Sangram Keshari Sahu"
__email__ = "sangramsahu15@gmail.com"
__license__ = "MIT"


import os
from tempfile import TemporaryDirectory

# Placeholder for optional parameters
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
params = snakemake.params.get("extra", "")

with TemporaryDirectory() as tempdir:
    os.system(
        f"(shovill"
        f" --assembler {snakemake.wildcards.assembler}"
        f" --outdir {tempdir} --force"
        f" --R1 {snakemake.input.r1}"
        f" --R2 {snakemake.input.r2}"
        f" --cpus {snakemake.threads}"
        f" {params}) {log}"
    )

    os.system(
        f"mv {tempdir}/{snakemake.wildcards.assembler}.fasta {snakemake.output.raw_assembly}"
        f" && mv {tempdir}/contigs.fa {snakemake.output.contigs}"
    )
