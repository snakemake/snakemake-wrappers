"""Snakemake wrapper for Kallisto index"""

__author__ = "Joël Simoneau"
__copyright__ = "Copyright 2019, Joël Simoneau"
__email__ = "simoneaujoel@gmail.com"
__license__ = "MIT"

import os

# Creating log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")

# Allowing for multiple FASTA files
fasta = snakemake.input.get("fasta")
assert fasta is not None, "input-> a FASTA-file is required"
fasta = " ".join(fasta) if isinstance(fasta, list) else fasta

os.system(
    f"kallisto index "  # Tool
    f"{extra} "  # Optional parameters
    f"--index={snakemake.output.index} "  # Output file
    f"{fasta} "  # Input FASTA files
    f"{log}"  # Logging
)
