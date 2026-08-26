"""Snakemake wrapper for DotMatch CRISPR guide counting."""

__author__ = "Donncha O'Toole"
__license__ = "MIT"

from shlex import quote

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

summary = snakemake.output.get("summary")
if summary:
    summary = f"--summary {quote(summary)}"

sample_qc = snakemake.output.get("sample_qc")
if sample_qc:
    sample_qc = f"--sample-qc {quote(sample_qc)}"

shell("dotmatch crispr-count "
    "--library {snakemake.input.library:q} "
    "--samples {snakemake.input.samples:q} "
    "--threads {snakemake.threads} "
    "--out {snakemake.output.counts:q} "
    "{summary} "
    "{sample_qc} "
    "{extra}"
    " {log}"
)
