__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")


shell(
    "(bamToBed"
    " {extra}"
    " -i {snakemake.input[0]}"
    " > {snakemake.output[0]}"
    ") {log}"
)
