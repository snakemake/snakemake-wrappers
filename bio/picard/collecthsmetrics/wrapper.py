"""Snakemake wrapper for picard CollectHSMetrics."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


inputs = " ".join("INPUT={}".format(in_) for in_ in snakemake.input)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "picard CollectHsMetrics"
    " {extra}"
    " INPUT={snakemake.input[0]}"
    " OUTPUT={snakemake.output[0]}"
    " REFERENCE_SEQUENCE={snakemake.params.reference}"
    " BAIT_INTERVALS={snakemake.params.bait_intervals}"
    " TARGET_INTERVALS={snakemake.params.target_intervals}"
    " {log}")
