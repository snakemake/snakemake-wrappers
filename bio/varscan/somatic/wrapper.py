"""Snakemake wrapper for varscan somatic"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


import os.path as op

from snakemake.shell import shell
from snakemake.utils import makedirs

# Defining logging and gathering extra parameters
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
java_opts = ""
# Getting memory in megabytes, if java opts is not filled with -Xmx parameter
# By doing so, backward compatibility is preserved
if "mem_mb" in snakemake.resources.keys() and "-Xmx" not in extra:
    java_opts += " -Xmx{}M".format(snakemake.resources["mem_mb"])

# Getting memory in gigabytes, for user convenience. Please prefer the use
# of mem_mb over mem_gb as advised in documentation.
elif "mem_gb" in snakemake.resources.keys() and "-Xmx" not in extra:
    java_opts += " -Xmx{}G".format(snakemake.resources["mem_gb"])

# Getting java temp directory from output files list, if -Djava.io.tmpdir
# is not provided in java parameters. By doing so, backward compatibility is
# not broken.
if "java_temp" in snakemake.output.keys() and "-Djava.io.tmpdir" not in extra:
    java_opts += " -Djava.io.tmpdir={}".format(snakemake.output["java_temp"])

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
