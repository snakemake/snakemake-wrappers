"""Snakemake wrapper for varscan somatic"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


import os
import os.path as op

# Defining logging and gathering extra parameters
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

# Building output dirs
os.makedirs(op.dirname(snakemake.output.snp))
os.makedirs(op.dirname(snakemake.output.indel))

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

os.system(
    f"varscan somatic"  # Tool and its subcommand
    f" {in_pileup}"  # Path to input file(s)
    f" {prefix}"  # Path to output
    f" {extra}"  # Extra parameters
    f" {mpileup}"
    f" --output-snp {snakemake.output.snp}"  # Path to snp output file
    f" --output-indel {snakemake.output.indel}"  # Path to indel output file
)
