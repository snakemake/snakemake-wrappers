"""
Snakemake Wrapper for PyTRF extract
------------------------------------------------------
Extract tandem repeat sequences with flanking regions.
"""

from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format, is_arg


# Logging
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Get input file
try:
    input_file = Path(snakemake.input.ref).resolve()
    repeat_file = Path(snakemake.input.repeat).resolve()
except (AttributeError, TypeError) as e:
    raise ValueError(
        f"Input specification error: {e}. "
        "Expected named inputs: ref=<fasta/fastq>, repeat=<tsv/csv>"
    ) from e

# Get output file and determine format
try:
    output_file = Path(snakemake.output[0]).resolve()
except (IndexError, TypeError) as e:
    raise ValueError("Output file is required") from e

out_format = get_format(output_file)

supported_formats = {"tsv", "csv", "fasta"}

if out_format not in supported_formats:
    raise ValueError(
        f"Unsupported format '{out_format}' for pytrf extract. "
        f"Supported formats: {', '.join(supported_formats)}"
    )

# Additional parameters
extra = snakemake.params.get("extra", "")

if is_arg("-f", extra) or is_arg("--out-format", extra):
    raise ValueError(
        "Output format is automatically inferred from output file extension. "
        "Do not specify -f/--out-format in params.extra. "
    )

if is_arg("-r", extra) or is_arg("--repeat-file", extra):
    raise ValueError(
        "Repeat file should be specified as an input. "
        "Do not specify -r/--repeat-file in params.extra"
    )

# Execute
try:
    shell("pytrf extract"
        " {input_file}"
        " -r {repeat_file}"
        " {extra}"
        " -f {out_format}"
        " -o {output_file}"
        " {log}"
    )
except Exception as e:
    raise RuntimeError(f"PyTRF extract execution failed: {e}") from e
