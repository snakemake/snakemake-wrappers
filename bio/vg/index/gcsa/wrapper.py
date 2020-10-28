__author__ = "Ali Ghaffaari"
__copyright__ = "Copyright 2017, Ali Ghaffaari"
__email__ = "ghaffari@mpi-inf.mpg.de"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell()

shell(
    "(vg index -g {snakemake.output.gcsa} --threads {snakemake.threads}"
    " {snakemake.params} {snakemake.input.vgs}) {log}"
)
