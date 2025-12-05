"""
Snakemake Wrapper for PyTRF findgtr
------------------------------------------------------
Find exact generic tandem repeats (any motif size).
"""

from pathlib import Path
from snakemake.shell import shell

# Logging
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Get input file
try:
    input_file = Path(snakemake.input[0]).resolve()
except (IndexError, TypeError) as e:
    raise ValueError(f"Input specification error: {e}") from e

# Get output file if specified
OUTPUT_FILE = None
if snakemake.output:
    OUTPUT_FILE = Path(snakemake.output[0]).resolve()

# Build parameters
params = []

if hasattr(snakemake.params, "out_format"):
    params.append(f"-f {snakemake.params.out_format}")

if hasattr(snakemake.params, "min_motif"):
    params.append(f"-m {snakemake.params.min_motif}")

if hasattr(snakemake.params, "max_motif"):
    params.append(f"-M {snakemake.params.max_motif}")

if hasattr(snakemake.params, "min_repeat"):
    params.append(f"-r {snakemake.params.min_repeat}")

if hasattr(snakemake.params, "min_length"):
    params.append(f"-l {snakemake.params.min_length}")

# Build command
CMD = f"pytrf findgtr {input_file}"
if params:
    CMD += " " + " ".join(params)
if OUTPUT_FILE:
    CMD += f" -o {OUTPUT_FILE}"

# Execute
try:
    shell(f"{CMD} {log}")
except Exception as e:
    raise RuntimeError(f"pytrf findgtr execution failed: {e}") from e
