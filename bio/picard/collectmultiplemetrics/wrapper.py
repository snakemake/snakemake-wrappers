__author__ = "David Laehnemann, Antonie Vietor"
__copyright__ = "Copyright 2020, David Laehnemann, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import sys
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

res = snakemake.resources.get("mem_gb", "3")
if not res or res is None:
    res = 3

progs = set()
extensions = set()

for file in snakemake.output:
    if "alignment_summary" in file:
        progs.add("CollectAlignmentSummaryMetrics ")
        extensions.add(".alignment_summary_metrics")
    elif "insert_size" in file:
        progs.add("CollectInsertSizeMetrics ")
        extensions.add(".insert_size_metrics")
        extensions.add(".insert_size_histogram.pdf")
    elif "quality_distribution" in file:
        progs.add("QualityScoreDistribution ")
        extensions.add(".quality_distribution_metrics")
        extensions.add(".quality_distribution.pdf")
    elif "quality_by_cycle" in file:
        progs.add("MeanQualityByCycle ")
        extensions.add(".quality_by_cycle_metrics")
        extensions.add(".quality_by_cycle.pdf")
    elif "base_distribution_by_cycle" in file:
        progs.add("CollectBaseDistributionByCycle ")
        extensions.add(".base_distribution_by_cycle_metrics")
        extensions.add(".base_distribution_by_cycle.pdf")
    elif "gc_bias" in file:
        progs.add("CollectGcBiasMetrics ")
        extensions.add(".gc_bias.detail_metrics")
        extensions.add(".gc_bias.summary_metrics")
        extensions.add(".gc_bias.pdf")
    elif "rna_metrics" in file:
        progs.add("RnaSeqMetrics ")
        extensions.add(".rna_metrics")
    elif "bait_bias" in file or "error_summary" in file or "pre_adapter" in file:
        progs.add("CollectSequencingArtifactMetrics ")
        extensions.add(".bait_bias_detail_metrics")
        extensions.add(".bait_bias_summary_metrics")
        extensions.add(".error_summary_metrics")
        extensions.add(".pre_adapter_detail_metrics")
        extensions.add(".pre_adapter_summary_metrics")
    elif "quality_yield" in file:
        progs.add("CollectQualityYieldMetrics ")
        extensions.add(".quality_yield_metrics")
    else:
        sys.exit(
            "Unknown type of metrics file requested, for possible metrics files, see https://snakemake-wrappers.readthedocs.io/en/stable/wrappers/picard/collectmultiplemetrics.html"
        )
programs = " PROGRAM=" + "PROGRAM=".join(progs)

out = str(snakemake.wildcards.sample)  # as default
output_file = str(snakemake.output[0])
for ext in extensions:
    if ext in output_file:
        if output_file.endswith(ext):
            out = output_file[: -len(ext)]
            break

shell(
    "(picard -Xmx{res}g CollectMultipleMetrics "
    "I={snakemake.input.bam} "
    "O={out} "
    "R={snakemake.input.ref} "
    "{snakemake.params}{programs}) {log}"
)
