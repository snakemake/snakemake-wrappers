__author__ = "Max Cummins"
__copyright__ = "Copyright 2021, Max Cummins"
__email__ = "max.l.cummins@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "mlst"
    " {snakemake.params.extra}"
    " {snakemake.input.assembly}"
    " > {snakemake.output.mlst}"
    " {log}"
)
