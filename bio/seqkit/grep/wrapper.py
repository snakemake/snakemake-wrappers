__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    "seqkit grep"
    " --threads {snakemake.threads}"
    " --pattern-file {snakemake.input.patterns}"
    " {extra}"
    " --out-file {snakemake.output.fastx}"
    " {snakemake.input.fastx}"
    " {log}"
)
