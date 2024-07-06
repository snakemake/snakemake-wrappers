__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
subcommand = snakemake.params["subcommand"]
extra = snakemake.params.get("extra", "")

# Input TSV delimiter
if len(snakemake.input) == 1:
    if str(snakemake.input).removesuffix(".gz").endswith(".tsv"):
        extra += " --tabs"
elif all(input.removesuffix(".gz").endswith(".tsv") for input in snakemake.input):
    extra += " --tabs"


# Output TSV delimiter
if len(snakemake.output) == 1:
    if str(snakemake.output).removesuffix(".gz").endswith(".tsv"):
        extra += " --out-tabs"
elif all(output.removesuffix(".gz").endswith(".tsv") for output in snakemake.output):
    extra += " --out-tabs"


shell(
    "csvtk {subcommand} --num-cpus {snakemake.threads} {extra} --out-file {snakemake.output} {snakemake.input} {log}"
)
