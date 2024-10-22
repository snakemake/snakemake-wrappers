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


# Function to validate output file extensions and get common prefix
def get_prefix(files):
    # Check all files have the same dirname
    dirname = os.path.dirname(files[0])
    if not all(os.path.dirname(f) == dirname for f in files):
        raise ValueError("Output files must all share the same output directory path.")

    # Valid file extensions from hisat2-build docs
    ht2_extensions = {f".{i}.ht2" for i in range(1, 9)}
    ht2l_extensions = {f".{i}.ht2l" for i in range(1, 9)}
    all_extensions = ht2_extensions | ht2l_extensions

    # Get user file extensions
    extensions = []
    for file in files:
        for ext in all_extensions:
            if file.endswith(ext):
                extensions.append(ext)

    # Check all 8 files are specified in the output with the correct extensions
    if all(ht2 in extensions for ht2 in ht2_extensions) or all(
        ht2l in extensions for ht2l in ht2l_extensions
    ):
        prefix = os.path.commonprefix(list(files)).rstrip(".")
    else:
        raise ValueError(
            "Output files must have either '.ht2' or '.ht2l' extensions for all 8 files."
        )

    if not prefix:
        raise ValueError("All output files must share the same prefix.")

    return prefix


# get common prefix
prefix = get_prefix(snakemake.output)

# make output directory
if os.path.dirname(prefix):
    os.makedirs(os.path.dirname(prefix), exist_ok=True)

shell(
    "hisat2-build {extra} " "-p {snakemake.threads} " "{input_seq} " "{prefix} " "{log}"
)
