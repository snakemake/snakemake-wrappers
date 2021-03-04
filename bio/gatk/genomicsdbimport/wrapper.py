__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"


import os

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

gvcfs = list(map("--variant {}".format, snakemake.input.gvcfs))

db_action = snakemake.params.get("db_action", "create")
if db_action == "create":
    db_action = "--genomicsdb-workspace-path"
elif db_action == "update":
    db_action = "--genomicsdb-update-workspace-path"
else:
    raise ValueError(
        "invalid option provided to 'params.db_action'; please choose either 'create' or 'update'."
    )

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "gatk --java-options '{java_opts}' GenomicsDBImport {extra} "
    "{gvcfs} "
    "--intervals {snakemake.params.intervals} "
    "{db_action} {snakemake.output.db} {log}"
)
