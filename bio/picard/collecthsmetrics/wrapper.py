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
    " INPUT={snakemake.input.bam[0]}"
    " OUTPUT={snakemake.output[0]}"
    " REFERENCE_SEQUENCE={snakemake.input.reference[0]}"
    " BAIT_INTERVALS={snakemake.input.bait_intervals[0]}"
    " TARGET_INTERVALS={snakemake.input.target_intervals[0]}"
    " {log}")
