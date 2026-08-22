"""Snakemake wrapper for DotMatch CRISPR guide counting."""

__author__ = "Donncha O'Toole"
__license__ = "MIT"

from shlex import quote

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
guide_start = snakemake.params.guide_start
guide_length = snakemake.params.guide_length
k = snakemake.params.get("k", 1)
metric = snakemake.params.get("metric", "hamming")
ambiguity_policy = snakemake.params.get("ambiguity_policy", "radius")
ambiguous = snakemake.params.get("ambiguous", "discard")
threads = snakemake.threads
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

indel_window = snakemake.params.get("indel_window")
indel_window_arg = ""
if indel_window is not None:
    indel_window_arg = f"--indel-window {indel_window}"

summary_arg = ""
summary = snakemake.output.get("summary")
if summary:
    summary_arg = f"--summary {quote(summary)}"

sample_qc_arg = ""
sample_qc = snakemake.output.get("sample_qc")
if sample_qc:
    sample_qc_arg = f"--sample-qc {quote(sample_qc)}"

shell(
    "(dotmatch crispr-count "
    "--library {snakemake.input.library:q} "
    "--samples {snakemake.input.samples:q} "
    "--guide-start {guide_start} "
    "--guide-length {guide_length} "
    "--k {k} "
    "--metric {metric} "
    "--ambiguity-policy {ambiguity_policy} "
    "--ambiguous {ambiguous} "
    "--threads {threads} "
    "--out {snakemake.output.counts:q} "
    "{summary_arg} "
    "{sample_qc_arg} "
    "{indel_window_arg} "
    "{extra}) {log}"
)
