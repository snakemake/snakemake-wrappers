__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
subcommand = snakemake.params["subcommand"]
extra = snakemake.params.get("extra", "")

# TSV delimiter
if len(snakemake.input["table"]) == 1:
    if str(snakemake.input["table"]).endswith(".tsv"):
        extra += " --delimiter $'\t' "
elif all(str(table).endswith(".tsv") for table in snakemake.input["table"]):
    extra += " --delimiter $'\t' "


# Automatic multithreading when possible
if subcommand in ["frequency", "split", "stats"]:
    extra += f" --jobs {snakemake.threads} "
elif snakemake.threads > 1:
    raise Warning("Only one thread is required")

# Command line building
if subcommand == "join":
    shell(
        "xsv {subcommand} {extra} "
        "{snakemake.params.col1} {snakemake.input.table[0]} "
        "{snakemake.params.col2} {snakemake.input.table[1]} "
        "> {snakemake.output} {log}"
    )
elif subcommand == "index":
    log = snakemake.log_fmt_shell(stdout=True, stderr=True)
    shell("xsv {subcommand} {extra} {snakemake.input.table} {log}")
elif subcommand == "split":
    log = snakemake.log_fmt_shell(stdout=True, stderr=True)
    outdir = snakemake.output
    if len(outdir) > 1:
        outdir = os.path.dirname(outdir[0])
    shell("xsv {subcommand} {extra} {outdir} {snakemake.input.table} {log}")
else:
    shell(
        "xsv {subcommand} {extra} {snakemake.input.table} "
        " > {snakemake.output} {log}"
    )
