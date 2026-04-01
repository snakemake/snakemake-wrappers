"""
Snakemake Wrapper for PyTRF
------------------------------------------------------
Tandem repeat finding and extraction toolkit.
Supports: findstr, findgtr, findatr, extract subcommands.
"""

from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format, is_arg

# Configuration variables
VALID_SUBCOMMANDS = {"findstr", "findgtr", "findatr", "extract"}
FORMAT_SUPPORT = {
    "findstr": {"tsv", "csv", "bed", "gff"},
    "findgtr": {"tsv", "csv", "gff"},
    "findatr": {"tsv", "csv", "gff"},
    "extract": {"tsv", "csv", "fasta"},
}

# Logging
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Get subcommand type and validate
subcommand = snakemake.params.get("subcommand")
if subcommand is None or subcommand not in VALID_SUBCOMMANDS:
    raise ValueError(
        f"Invalid subcommand '{subcommand}'. "
        f"Valid options: {', '.join(sorted(VALID_SUBCOMMANDS))}"
    )

# Get sequence input (all commands use named input 'seq')
try:
    input_file = Path(snakemake.input.seq).resolve()
except (AttributeError, TypeError) as e:
    raise ValueError(
        f"Input specification error: {e}. " "Expected named input: seq=<fasta/fastq>"
    ) from e

# Get repeat file (extract only)
repeat_file = None
if subcommand == "extract":
    try:
        repeat_file = Path(snakemake.input.repeat).resolve()
    except (AttributeError, TypeError) as e:
        raise ValueError(
            f"Input specification error: {e}. "
            "extract requires second input: repeat=<tsv/csv>"
        ) from e

# Get output file
try:
    output_file = Path(snakemake.output[0]).resolve()
except (IndexError, TypeError) as e:
    raise ValueError("Output file is required") from e

# Infer and validate output format
out_format = get_format(output_file)
supported_formats = FORMAT_SUPPORT[subcommand]
if out_format not in supported_formats:
    raise ValueError(
        f"Unsupported format '{out_format}' for pytrf {subcommand}. "
        f"Supported formats: {', '.join(sorted(supported_formats))}"
    )

# Get extra parameters
extra = snakemake.params.get("extra", "")

# Validate: block format and output flags (all subcommands)
if (
    is_arg("-f", extra)
    or is_arg("--out-format", extra)
    or is_arg("-o", extra)
    or is_arg("--out-file", extra)
):
    raise ValueError(
        "Output format is inferred and output path is provided through Snakemake. "
        "Do not specify -f/--out-format or -o/--out-file in params.extra"
    )

# Validate: block repeat-file flag (extract only)
if subcommand == "extract" and (is_arg("-r", extra) or is_arg("--repeat-file", extra)):
    raise ValueError(
        "Repeat file is provided as input.repeat. "
        "Do not specify -r/--repeat-file in params.extra"
    )

# Build repeat file argument (empty string for non-extract commands)
repeat_arg = f" -r {repeat_file}" if subcommand == "extract" else ""

# Execute
try:
    shell(
        "pytrf {subcommand}"
        " {input_file}"
        "{repeat_arg}"
        " {extra}"
        " -f {out_format}"
        " -o {output_file}"
        " {log}"
    )
except Exception as e:
    raise RuntimeError(f"pytrf {subcommand} execution failed: {e}") from e
