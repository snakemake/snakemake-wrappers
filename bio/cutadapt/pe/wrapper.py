"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


n = len(snakemake.input)
assert n == 2, "Input must contain 2 (paired-end) elements."

extra = snakemake.params.get("extra", "")
adapters = snakemake.params.get("adapters", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

assert (
    extra != "" or adapters != ""
), "No options provided to cutadapt. Please use 'params: adapters=' or 'params: extra='."

shell(
    "cutadapt"
    " {adapters}"
    " {extra}"
    " -o {snakemake.output.fastq1}"
    " -p {snakemake.output.fastq2}"
    " -j {snakemake.threads}"
    " {snakemake.input}"
    " > {snakemake.output.qc} {log}"
)
