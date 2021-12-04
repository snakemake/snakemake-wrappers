__author__ = "Kim Philipp Jablonski, Nikos Tsardakas Renhuldt"
__copyright__ = "Copyright 2020, Kim Philipp Jablonski, Nikos Tsardakas Renhuldt"
__email__ = "kim.philipp.jablonski@gmail.com, nikos.tsardakas_renhuldt@tbiokem.lth.se"
__license__ = "MIT"


from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


shell(
    "diamond blastp"
    " --threads {snakemake.threads}"
    " --db {snakemake.input.fname_db}"
    " --query {snakemake.input.fname_fasta}"
    " --out {snakemake.output.fname}"
    " {extra}"
    " {log}"
)
