"""Snakemake wrapper for shovill."""

__author__ = "Sangram Keshari Sahu"
__copyright__ = "Copyright 2020, Sangram Keshari Sahu"
__email__ = "sangramsahu15@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory

# Placeholder for optional parameters
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
params = snakemake.params.get("extra", "")

with TemporaryDirectory() as tempdir:
    shell(
        "(shovill"
        " --assembler {snakemake.wildcards.assembler}"
        " --outdir {tempdir} --force"
        " --R1 {snakemake.input.r1}"
        " --R2 {snakemake.input.r2}"
        " --cpus {snakemake.threads}"
        " {params}) {log}"
    )

    shell(
        "mv {tempdir}/{snakemake.wildcards.assembler}.fasta {snakemake.output.raw_assembly}"
        " && mv {tempdir}/contigs.fa {snakemake.output.contigs}"
    )
