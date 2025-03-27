__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
subcommand = snakemake.params["subcommand"]
extra = snakemake.params.get("extra", "")


# Input file delimiter
in_files = [Path(snakemake.input[0])] if len(snakemake.input) == 1 else [Path(in_file) for in_file in snakemake.input]
if all(get_format(in_file) == "tsv" for in_file in in_files if in_file.suffix):
    extra += " --tabs"


# Output file delimiter
out_files = [Path(snakemake.output[0])] if len(snakemake.output) == 1 else [Path(out_file) for out_file in snakemake.output]
if all(get_format(out_file) == "tsv" for out_file in out_files if out_file.suffix):
    extra += " --out-tabs"


shell(
    "csvtk {subcommand} --num-cpus {snakemake.threads} {extra} --out-file {snakemake.output} {snakemake.input} {log}"
)
