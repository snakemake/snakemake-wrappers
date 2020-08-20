"""Snakemake wrapper for GATK4 Mutect2"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")

os.system(
    f"gatk Mutect2 "  # Tool and its subprocess
    f"--input {snakemake.input.map} "  # Path to input mapping file
    f"--output {snakemake.output.vcf} "  # Path to output vcf file
    f"--reference {snakemake.input.fasta} "  # Path to reference fasta file
    f"{extra} "  # Extra parameters
    f"{log}"  # Logging behaviour
)
