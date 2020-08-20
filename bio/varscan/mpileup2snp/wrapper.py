"""Snakemake wrapper for Varscan2 mpileup2snp"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import os
import os.path as op

# Gathering extra parameters and logging behaviour
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

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
os.makedirs(op.dirname(snakemake.output[0]))

os.system(
    f"varscan mpileup2snp "  # Tool and its subprocess
    "{extra} "  # Extra parameters
    "<( {pileup} ) "
    "> {snakemake.output[0]} "  # Path to vcf file
    "{log}"  # Logging behaviour
)
