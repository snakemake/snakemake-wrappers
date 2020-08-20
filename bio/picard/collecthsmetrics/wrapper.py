"""Snakemake wrapper for picard CollectHSMetrics."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


import os


inputs = " ".join("INPUT={}".format(in_) for in_ in snakemake.input)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    f"picard CollectHsMetrics"
    f" {extra}"
    f" INPUT={snakemake.input.bam}"
    f" OUTPUT={snakemake.output[0]}"
    f" REFERENCE_SEQUENCE={snakemake.input.reference}"
    f" BAIT_INTERVALS={snakemake.input.bait_intervals}"
    f" TARGET_INTERVALS={snakemake.input.target_intervals}"
    f" {log}"
)
