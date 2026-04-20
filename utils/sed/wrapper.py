__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2026, Filipe G. Vieira"
__license__ = "MIT"

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

shell(
    "sed {extra} {snakemake.params.expr:q} {snakemake.input[0]} > {snakemake.output[0]} {log}"
)
