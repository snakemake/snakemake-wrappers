"""Snakemake wrapper for varscan somatic"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


import os.path as op

from snakemake.shell import shell
from snakemake.utils import makedirs
from snakemake_wrapper_utils.java import get_java_opts

# Defining logging and gathering extra parameters
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

# Building output dirs
makedirs(op.dirname(snakemake.output.snp))
makedirs(op.dirname(snakemake.output.indel))

# Output prefix
prefix = op.splitext(snakemake.output.snp)[0]

# Searching for input files
pileup_pair = ["normal_pileup", "tumor_pileup"]

in_pileup = ""
mpileup = ""
if "mpileup" in snakemake.input.keys():
    # Case there is a mpileup with both normal and tumor
    in_pileup = snakemake.input.mpileup
    mpileup = "--mpileup 1"
elif all(pileup in snakemake.input.keys() for pileup in pileup_pair):
    # Case there are two separate pileup files
    in_pileup = " {snakemake.input.normal_pileup}" " {snakemakeinput.tumor_pileup} "
else:
    raise KeyError("Could not find either a mpileup, or a pair of pileup files")

shell(
    "varscan somatic"  # Tool and its subcommand
    " {in_pileup}"  # Path to input file(s)
    " {prefix}"  # Path to output
    " {java_opts} {extra}"  # Extra parameters
    " {mpileup}"
    " --output-snp {snakemake.output.snp}"  # Path to snp output file
    " --output-indel {snakemake.output.indel}"  # Path to indel output file
)
