__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"

import snakemake # type: ignore
from snakemake.shell import shell # type: ignore

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

compress = "| gzip" if snakemake.output[0].endswith(".gz") else ""

shell(
    "(bamToBed"
    " {extra}"
    " -i {snakemake.input[0]}"
    " {compress}"
    " > {snakemake.output[0]}"
    ") {log}"
)
