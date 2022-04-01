__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from pathlib import Path
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Prefix that should be used for the database
prefix = Path(snakemake.output[0]).parent


shell(
    "dragen-os"
    " --ht-num-threads {snakemake.threads}"
    " --build-hash-table true"
    " --ht-reference {snakemake.input[0]}"
    " --output-directory {prefix}"
    " {extra}"
    " {log}"
)
