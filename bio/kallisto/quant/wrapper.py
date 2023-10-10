"""Snakemake wrapper for Kallisto quant"""

__author__ = "Joël Simoneau"
__copyright__ = "Copyright 2019, Joël Simoneau"
__email__ = "simoneaujoel@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

# Creating log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")

# Allowing for multiple FASTQ files
fastq = snakemake.input.get("fastq")
assert fastq is not None, "input-> a FASTQ-file is required"
fastq = " ".join(fastq) if isinstance(fastq, list) else fastq

shell(
    "kallisto quant "  # Tool
    " --threads {snakemake.threads}"  # Number of threads
    " --index {snakemake.input.index}"  # Input file
    " {extra}"  # Optional parameters
    " --output-dir {snakemake.output}"  # Output directory
    " {fastq}"  # Input FASTQ files
    " {log}"  # Logging
)
