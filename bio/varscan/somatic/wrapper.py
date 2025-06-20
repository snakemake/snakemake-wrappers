"""Snakemake wrapper for varscan somatic"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


import os

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

# Defining logging and gathering extra parameters
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

# Output prefix
prefix = os.path.splitext(snakemake.output.snp)[0]

# Case there is a mpileup with both normal and tumor
mpileup = "--mpileup 1" if len(snakemake.input) == 1 else ""

shell(
    "varscan somatic"  # Tool and its subcommand
    " {snakemake.input}"  # Path to input file(s)
    " {prefix}"  # Path to output
    " {java_opts}"  # Java options
    " {extra}"  # Extra parameters
    " {mpileup}"
    " --output-snp {snakemake.output.snp}"  # Path to snp output file
    " --output-indel {snakemake.output.indel}"  # Path to indel output file
    " {log}"
)
