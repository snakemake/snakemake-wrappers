# coding: utf-8

"""Snakemake wrapper for all grit subcommands"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2026, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

command = snakemake.params["command"]
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

input_args = ""
output_args = f" > {snakemake.output[0]}"
if command in ("generate"):
    output_args = f" --output {snakemake.output[0]}"
    log = snakemake.log_fmt_shell(stdout=True, stderr=True)
elif command in ("sort", "merge", "slop", "complement", "genomecov", "multiinter"):
    input_args = f" --input {snakemake.input.bed}"
elif command in ("coverage", "intersect", "closest", "window", "jaccard", "subtract"):
    input_args = f"--file-a {snakemake.input.bed[0]} --file-b {snakemake.input.bed[1]}"
else:
    raise (f"Unknown command {command}")


genome = snakemake.input.get("genome")
if genome and (not command in ("jaccard", "multiinter")):
    extra += f" --genome {genome}"


shell(
    "grit {command} {extra} "
    "--threads {snakemake.threads} "
    "{input_args} {output_args} {log}"
)
