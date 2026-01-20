"""
Snakemake Wrapper for PyTRF findgtr
------------------------------------------------------
Find exact generic tandem repeats (any motif size).
"""

from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import is_arg


# Logging
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Get input file
try:
    input_file = Path(snakemake.input[0]).resolve()
except (IndexError, TypeError) as e:
    raise ValueError(f"Input specification error: {e}") from e

# Get output file and determine format
try:
    OUTPUT_FILE = Path(snakemake.output[0]).resolve()
except (IndexError, TypeError) as e:
    raise ValueError("Output file is required") from e

ext = OUTPUT_FILE.suffix.lower()

format_map = {
    ".tsv": "tsv",
    ".csv": "csv",
    ".gff": "gff",
}

if ext not in format_map:
    raise ValueError(
        f"Unsupported output format '{ext}' for pytrf findgtr. "
        f"Supported extensions: {', '.join(format_map.keys())}"
    )

out_format = format_map[ext]

# Additional parameters
extra = snakemake.params.get("extra", "")

if is_arg("-f", extra) or is_arg("--out-format", extra):
    raise ValueError(
        "Output format is automatically inferred from output file extension. "
        "Do not specify -f/--out-format in params.extra. "
        f"Detected format: {out_format} (from {ext})"
    )

# Build command
CMD = f"pytrf findgtr {input_file} -f {out_format}"
if extra:
    CMD += f" {extra}"
CMD += f" -o {OUTPUT_FILE}"

# Execute
try:
    shell(f"{CMD} {log}")
except Exception as e:
    raise RuntimeError(f"pytrf findgtr execution failed: {e}") from e
