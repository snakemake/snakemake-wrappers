"""Snakemake wrapper for GATK4 Mutect2"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake.utils import makedirs
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bam_output = "--bam-output"
if snakemake.output.get("bam", None) is not None:
    bam_output = bam_output + " " + snakemake.output.bam
else:
    bam_output = ""

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

shell(
    "gatk --java-options '{java_opts}' Mutect2 "  # Tool and its subprocess
    "--input {snakemake.input.map} "  # Path to input mapping file
    "{bam_output} "  # Path to output bam file, optional
    "--output {snakemake.output.vcf} "  # Path to output vcf file
    "--reference {snakemake.input.fasta} "  # Path to reference fasta file
    "{extra} "  # Extra parameters
    "{log}"  # Logging behaviour
)
