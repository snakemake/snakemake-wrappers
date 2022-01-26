__author__ = "Nikos Tsardakas Renhuldt"
__copyright__ = "Copyright 2021, Nikos Tsardakas Renhuldt"
__email__ = "nikos.tsardakas_renhuldt@tbiokem.lth.se"
__license__ = "MIT"


from snakemake.shell import shell
import os

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

shell(
    "fasttree "
    "{extra} "
    "{snakemake.input.alignment} "
    "> {snakemake.output.tree} "
    "{log}"
)
