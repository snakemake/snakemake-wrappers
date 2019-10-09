"""Snakemake wrapper for picard CollectHSMetrics."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


inputs = " ".join("INPUT={}".format(in_) for in_ in snakemake.input)
extra = snakemake.params.get("extra", "")
java_options = snakemake.params.get("java_options", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "picard {java_options} CollectHsMetrics"
    " {extra}"
    " INPUT={snakemake.input.bam}"
    " OUTPUT={snakemake.output[0]}"
    " REFERENCE_SEQUENCE={snakemake.input.reference}"
    " BAIT_INTERVALS={snakemake.input.bait_intervals}"
    " TARGET_INTERVALS={snakemake.input.target_intervals}"
    " {log}")
