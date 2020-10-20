"""Snakemake wrapper for Varscan2 mpileup2snp"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import os.path as op
from snakemake.shell import shell
from snakemake.utils import makedirs

# Gathering extra parameters and logging behaviour
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
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

# In case input files are gzipped mpileup files,
# they are being unzipped and piped
# In that case, it is recommended to use at least 2 threads:
# - One for unzipping with zcat
# - One for running varscan
pileup = (
    " cat {} ".format(snakemake.input[0])
    if not snakemake.input[0].endswith("gz")
    else " zcat {} ".format(snakemake.input[0])
)

# Building output directories
makedirs(op.dirname(snakemake.output[0]))

shell(
    "varscan mpileup2snp "  # Tool and its subprocess
    "<( {pileup} ) "
    "{java_opts} {extra} "  # Extra parameters
    "> {snakemake.output[0]} "  # Path to vcf file
    "{log}"  # Logging behaviour
)
