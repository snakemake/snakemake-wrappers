"""Snakemake wrapper for shovill."""

__author__ = "Sangram Keshari Sahu"
__copyright__ = "Copyright 2020, Sangram Keshari Sahu"
__email__ = "sangramsahu15@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell
from tempfile import TemporaryDirectory

# Placeholder for optional parameters
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
params = snakemake.params.get("extra", "")

# Determine the assembler from wildcard of output file name
assembler = path.basename(snakemake.output.raw_assembly).split(".")[1]

with TemporaryDirectory() as tempdir:
    shell(
        "(shovill"
        " --assembler {assembler}"
        " --outdir {tempdir} --force"
        " --R1 {snakemake.input.r1}"
        " --R2 {snakemake.input.r2}"
        " --cpus {snakemake.threads}"
        " {params}) {log}"
    )

    outdir = path.dirname(snakemake.output.raw_assembly)

    shell(
        "mkdir {outdir}"
        " && mv {tempdir}/{assembler}.fasta {snakemake.output.raw_assembly}"
        " && mv {tempdir}/contigs.fa {snakemake.output.contigs}"
    )
