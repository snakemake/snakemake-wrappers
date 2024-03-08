"""Snakemake wrapper for MultiQC"""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


# No need for explicit temp folder, since MultiQC already uses TMPDIR (https://multiqc.info/docs/usage/troubleshooting/#no-space-left-on-device)

from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import is_arg


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Automatically detect configuration files when provided
# in input. For other ways to provide configuration to
# multiqc, see: https://multiqc.info/docs/getting_started/config/
mqc_config = snakemake.input.get("config", "")
if isinstance(mqc_config, list):
    for fp in mqc_config:
        extra += f" --config {fp}"
elif mqc_config:
    extra += f" --config {mqc_config}"


# Set this to False if multiqc should use the actual input directly
# instead of parsing the folders where the provided files are located
use_input_files_only = snakemake.params.get("use_input_files_only", False)
if not use_input_files_only:
    input_data = set(Path(fp).parent for fp in snakemake.input if fp not in mqc_config)
else:
    input_data = set(fp for fp in snakemake.input if fp not in mqc_config)


# Add extra options depending on output files
no_report = True
for output in snakemake.output:
    if output.endswith(".html"):
        no_report = False
    if output.endswith("_data"):
        extra += " --data-dir"
    if output.endswith(".zip"):
        extra += " --zip-data-dir"
if no_report:
    extra += " --no-report"
if (
    not is_arg("--data-dir", extra)
    and not is_arg("-z", extra)
    and not is_arg("--zip-data-dir", extra)
):
    extra += " --no-data-dir"

# Specify output dir and file name, since they are stored in the JSON file
out_dir = Path(snakemake.output[0]).parent
file_name = Path(snakemake.output[0]).with_suffix("").name


shell(
    "multiqc"
    " {extra}"
    " --outdir {out_dir}"
    " --filename {file_name}"
    " {input_data}"
    " {log}"
)


# Move files to another destination (if needed)
for output in snakemake.output:
    if output.endswith("_data"):
        ext = "_data"
    elif output.endswith(".zip"):
        ext = "_data.zip"
    else:
        ext = Path(output).suffix

    default_dest = f"{out_dir}/{file_name}{ext}"
    if default_dest != output:
        shell("mv {default_dest} {output}")
