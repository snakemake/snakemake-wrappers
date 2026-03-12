"""Snakemake wrapper for chopper."""

__author__ = "Artur Gomes"
__copyright__ = "Copyright 2026, Artur Gomes"
__email__ = "arafaelogomes@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Assert input
n = len(snakemake.input.in_reads)
assert (
    n == 1
), "input->sample must have 1 element."

reads = snakemake.input.in_reads[0]

outfile = snakemake.output.out_reads

shell(
    "chopper"
    " {extra}"
    " --input {reads:q}"
    " > {outfile:q}"
    " {log}"
)
