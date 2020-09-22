__author__ = "Ali Ghaffaari"
__copyright__ = "Copyright 2018, Ali Ghaffaari"
__email__ = "ali.ghaffaari@mpi-inf.mpg.de"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell()

shell(
    "(wgsim {snakemake.params} {snakemake.input.ref}"
    " {snakemake.output.read1} {snakemake.output.read2}) {log}"
)
