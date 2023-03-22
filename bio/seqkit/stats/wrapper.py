__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    "seqkit stats"
    " --threads {snakemake.threads}"
    " {extra}"
    " --out-file {snakemake.output.stats}"
    " {snakemake.input.fastx}"
    " {log}"
)
