"""Snakemake script for MSISensor Scan"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Extra parameters default value is an empty string
extra = snakemake.params.get("extra", "")

os.system(
    f"msisensor scan "  # Tool and its sub-command
    f"-d {snakemake.input} "  # Path to fasta file
    f"-o {snakemake.output} "  # Path to output file
    f"{extra} "  # Optional extra parameters
    f"{log}"  # Logging behavior
)
