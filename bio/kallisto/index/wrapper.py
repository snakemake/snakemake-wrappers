"""Snakemake wrapper for Kallisto index"""

__author__ = "Joël Simoneau"
__copyright__ = "Copyright 2019, Joël Simoneau"
__email__ = "simoneaujoel@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

# Creating log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")

# Allowing for multiple FASTA files
fasta = snakemake.input.get("fasta")
assert fasta is not None, "input-> a FASTA-file is required"
fasta = " ".join(fasta) if isinstance(fasta, list) else fasta

shell(
    "kallisto index"  # Tool
    " --threads {snakemake.threads}"
    " {extra}"  # Optional parameters
    " --index {snakemake.output.index}"  # Output file
    " {fasta}"  # Input FASTA files
    " {log}"  # Logging
)
