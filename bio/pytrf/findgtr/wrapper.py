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
output_file = None
if snakemake.output:
    output_file = Path(snakemake.output[0]).resolve()

# Build parameters
params = []

try:
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
except (AttributeError, ValueError) as e:
    raise RuntimeError(f"Parameter processing failed: {e}") from e

# Build command
cmd = f"pytrf findgtr {input_file}"
if params:
    cmd += " " + " ".join(params)
if output_file:
    cmd += f" -o {output_file}"

# Execute
try:
    shell(f"{cmd} {log}")
except Exception as e:
    raise RuntimeError(f"pytrf findgtr execution failed: {e}") from e
