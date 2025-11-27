"""
Snakemake Wrapper for PyTRF findstr
------------------------------------------------------
Find exact short tandem repeats (SSRs/microsatellites).
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

try:
    if hasattr(snakemake.params, "out_format"):
        params.append(f"-f {snakemake.params.out_format}")

    if hasattr(snakemake.params, "repeats"):
        repeats_list = snakemake.params.repeats
        if isinstance(repeats_list, (list, tuple)):
            REPEATS_STR = " ".join(str(x) for x in repeats_list)
            params.append(f"-r {REPEATS_STR}")
except (AttributeError, ValueError) as e:
    raise RuntimeError(f"Parameter processing failed: {e}") from e

# Build command
CMD = f"pytrf findstr {input_file}"
if params:
    CMD += " " + " ".join(params)
if OUTPUT_FILE:
    CMD += f" -o {OUTPUT_FILE}"

# Execute
try:
    shell(f"{CMD} {log}")
except Exception as e:
    raise RuntimeError(f"pytrf findstr execution failed: {e}") from e
