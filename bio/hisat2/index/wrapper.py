"""Snakemake wrapper for HISAT2 index"""

__author__ = "Joël Simoneau"
__copyright__ = "Copyright 2019, Joël Simoneau"
__email__ = "simoneaujoel@gmail.com"
__license__ = "MIT"

import os
from snakemake.shell import shell

# Creating log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")

# Allowing for multiple FASTA files
fasta = snakemake.input.get("fasta")
assert fasta is not None, "input-> a FASTA-file or a sequence is required"
input_seq = ""
if not "." in fasta:
    input_seq += "-c "
input_seq += ",".join(fasta) if isinstance(fasta, list) else fasta

# check that file prefix is not a path
prefix = snakemake.params.get("prefix", "")
assert "/" not in prefix, "params 'prefix' should be a filename prefix, not a path (do not include '/')."

# make output directory
outdir = snakemake.output[0]
os.makedirs(outdir, exist_ok=True)

shell(
    "hisat2-build {extra} "
    "-p {snakemake.threads} "
    "{input_seq} "
    "{outdir}/{prefix} "
    "{log}"
)
