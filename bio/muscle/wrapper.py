__author__ = "Nikos Tsardakas Renhuldt"
__copyright__ = "Copyright 2021, Nikos Tsardakas Renhuldt"
__email__ = "nikos.tsardakas_renhuldt@tbiokem.lth.se"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

mode = "-align"
if snakemake.params.get("super5"):
    mode = "-super5"

shell(
    "muscle"
    " -threads {snakemake.threads}"
    " {mode} {snakemake.input.fasta}"
    " {extra}"
    " -output {snakemake.output.alignment}"
    " {log}"
)
