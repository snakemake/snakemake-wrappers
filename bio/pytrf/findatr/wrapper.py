"""
Snakemake Wrapper for PyTRF findatr
------------------------------------------------------
Find approximate/imperfect tandem repeats.
"""

from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format, is_arg


# Logging
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Get input file
try:
    input_file = Path(snakemake.input[0]).resolve()
except (IndexError, TypeError) as e:
    raise ValueError(f"Input specification error: {e}") from e

# Get output file and determine format
try:
    output_file = Path(snakemake.output[0]).resolve()
except (IndexError, TypeError) as e:
    raise ValueError("Output file is required") from e

out_format = get_format(output_file)

supported_formats = {"tsv", "csv", "gff"}

if out_format not in supported_formats:
    raise ValueError(
        f"Unsupported format '{out_format}' for pytrf findatr. "
        f"Supported formats: {', '.join(supported_formats)}"
    )

# Additional parameters
extra = snakemake.params.get("extra", "")

# Validate: block format and output flags
if (
    is_arg("-f", extra)
    or is_arg("--out-format", extra)
    or is_arg("-o", extra)
    or is_arg("--out-file", extra)
):
    raise ValueError(
        "Output format is inferred and output path is provided by Snakemake output. "
        "Do not specify -f/--out-format or -o/--out-file in params.extra"
    )

# Execute
try:
    shell(
        "pytrf findatr"
        " {input_file}"
        " {extra}"
        " -f {out_format}"
        " -o {output_file}"
        " {log}"
    )
except Exception as e:
    raise RuntimeError(f"PyTRF findatr execution failed: {e}") from e
