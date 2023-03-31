__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"


import os
import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
# uses Java native library TileDB, which requires a lot of memory outside
# of the `-Xmx` memory, so we reserve 40% instead of the default 20%. See:
# https://gatk.broadinstitute.org/hc/en-us/articles/9570326648475-GenomicsDBImportGenomicsDBImport
java_opts = get_java_opts(snakemake, java_mem_overhead_factor=0.4)

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

intervals = snakemake.input.get("intervals")
if not intervals:
    intervals = snakemake.params.get("intervals")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' GenomicsDBImport"
        " {gvcfs}"
        " --intervals {intervals}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " {db_action} {snakemake.output.db}"
        " {log}"
    )
