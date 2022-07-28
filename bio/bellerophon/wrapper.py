__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


shell(
    "bellerophon"
    " --threads {snakemake.threads}"
    " --forward {snakemake.input.fwd}"
    " --reverse {snakemake.input.rev}"
    " {extra}"
    " --output {snakemake.output[0]}"
    " {log}"
)
