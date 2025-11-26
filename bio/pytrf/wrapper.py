"""
    Snakemake Wrapper for PyTRF
    ------------------------------------------------------
    A Python package for finding tandem repeats from genomic sequences.
"""

from pathlib import Path
from snakemake.shell import shell

# Get input and output files
input_file = Path(snakemake.input[0]).resolve()
output_file = Path(snakemake.output[0]).resolve()

# Set up logging
log = ""
if snakemake.log:
    log = f">{snakemake.log[0]} 2>&1"

# Get command from params (default to findstr)
command = snakemake.params.get("command", "findstr")

# Build basic command
cmd = f"pytrf {command} {input_file} -o {output_file}"

# Execute
print(f"[PYTRF-INFO] Running: {cmd}")
shell(f"{cmd} {log}")
print("[PYTRF-INFO] PyTRF wrapper completed successfully")