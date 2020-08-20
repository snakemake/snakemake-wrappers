"""Snakemake wrapper for Kallisto quant"""

__author__ = "Joël Simoneau"
__copyright__ = "Copyright 2019, Joël Simoneau"
__email__ = "simoneaujoel@gmail.com"
__license__ = "MIT"

import os

# Creating log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")

# Allowing for multiple FASTQ files
fastq = snakemake.input.get("fastq")
assert fastq is not None, "input-> a FASTQ-file is required"
fastq = " ".join(fastq) if isinstance(fastq, list) else fastq

os.system(
    f"kallisto quant "  # Tool
    f"{extra} "  # Optional parameters
    f"--threads={snakemake.threads} "  # Number of threads
    f"--index={snakemake.input.index} "  # Input file
    f"--output-dir={snakemake.output} "  # Output directory
    f"{fastq} "  # Input FASTQ files
    f"{log}"  # Logging
)
