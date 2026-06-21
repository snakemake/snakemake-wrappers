"""Snakemake wrapper for chopper."""

__author__ = "Artur Gomes"
__copyright__ = "Copyright 2026, Artur Gomes"
__email__ = "arafaelogomes@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

contam = snakemake.input.get("contam", "")
if contam:
    contam = f"--contam {contam}"

pipe_gz = "| gzip -c" if snakemake.output[0].endswith(".gz") else ""

shell(
    "chopper"
    " --threads {snakemake.threads}"
    " {contam}"
    " --input {snakemake.input.fq:q}"
    " {extra}"
    " {pipe_gz}"
    " > {snakemake.output[0]:q}"
    " {log}"
)
