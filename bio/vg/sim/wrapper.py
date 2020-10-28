__author__ = "Ali Ghaffaari"
__copyright__ = "Copyright 2018, Ali Ghaffaari"
__email__ = "ghaffari@mpi-inf.mpg.de"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False)

shell(
    "(vg sim {snakemake.params} --xg-name {snakemake.input.xg}"
    " --threads {snakemake.threads} > {snakemake.output.reads}) {log}"
)
