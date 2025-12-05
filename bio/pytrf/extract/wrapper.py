"""
Snakemake Wrapper for PyTRF extract
------------------------------------------------------
Extract tandem repeat sequences with flanking regions.
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

# Get repeat_file (required)
try:
    if not hasattr(snakemake.params, "repeat_file"):
        raise ValueError("Parameter 'repeat_file' is required for extract")
    repeat_file = Path(snakemake.params.repeat_file).resolve()
except (AttributeError, ValueError) as e:
    raise RuntimeError(f"Parameter validation failed: {e}") from e

# Build parameters
params = [f"-r {repeat_file}"]

if hasattr(snakemake.params, "out_format"):
    params.append(f"-f {snakemake.params.out_format}")

if hasattr(snakemake.params, "flank_length"):
    params.append(f"-l {snakemake.params.flank_length}")

# Build command
CMD = f"pytrf extract {input_file}"
if params:
    CMD += " " + " ".join(params)
if OUTPUT_FILE:
    CMD += f" -o {OUTPUT_FILE}"

# Execute
try:
    shell(f"{CMD} {log}")
except Exception as e:
    raise RuntimeError(f"PyTRF extract execution failed: {e}") from e
