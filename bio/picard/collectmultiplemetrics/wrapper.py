__author__ = "David Laehnemann, Antonie Vietor"
__copyright__ = "Copyright 2020, David Laehnemann, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import sys
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params
java_opts = ""
# Getting memory in megabytes, if java opts is not filled with -Xmx parameter
# By doing so, backward compatibility is preserved
if "mem_mb" in snakemake.resources.keys() and "-Xmx" not in extra:
    java_opts += " -Xmx{}M".format(snakemake.resources["mem_mb"])

# Getting memory in gigabytes, for user convenience. Please prefer the use
# of mem_mb over mem_gb as advised in documentation.
elif "mem_gb" in snakemake.resources.keys() and "-Xmx" not in extra:
    java_opts += " -Xmx{}G".format(snakemake.resources["mem_gb"])

# Previous wrapper set to 3 Gigabytes the default reserved memory.
# This behaviour is preseved below:
elif "-Xmx" not in extra:
    java_opts += " -Xmx3G"

# Getting java temp directory from output files list, if -Djava.io.tmpdir
# is not provided in java parameters. By doing so, backward compatibility is
# not broken.
if "java_temp" in snakemake.output.keys() and "-Djava.io.tmpdir" not in extra:
    java_opts += " -Djava.io.tmpdir={}".format(snakemake.output["java_temp"])

exts_to_prog = {
    ".alignment_summary_metrics": "CollectAlignmentSummaryMetrics",
    ".insert_size_metrics": "CollectInsertSizeMetrics",
    ".insert_size_histogram.pdf": "CollectInsertSizeMetrics",
    ".quality_distribution_metrics": "QualityScoreDistribution",
    ".quality_distribution.pdf": "QualityScoreDistribution",
    ".quality_by_cycle_metrics": "MeanQualityByCycle",
    ".quality_by_cycle.pdf": "MeanQualityByCycle",
    ".base_distribution_by_cycle_metrics": "CollectBaseDistributionByCycle",
    ".base_distribution_by_cycle.pdf": "CollectBaseDistributionByCycle",
    ".gc_bias.detail_metrics": "CollectGcBiasMetrics",
    ".gc_bias.summary_metrics": "CollectGcBiasMetrics",
    ".gc_bias.pdf": "CollectGcBiasMetrics",
    ".rna_metrics": "RnaSeqMetrics",
    ".bait_bias_detail_metrics": "CollectSequencingArtifactMetrics",
    ".bait_bias_summary_metrics": "CollectSequencingArtifactMetrics",
    ".error_summary_metrics": "CollectSequencingArtifactMetrics",
    ".pre_adapter_detail_metrics": "CollectSequencingArtifactMetrics",
    ".pre_adapter_summary_metrics": "CollectSequencingArtifactMetrics",
    ".quality_yield_metrics": "CollectQualityYieldMetrics",
}
progs = set()

for file in snakemake.output:
    matched = False
    for ext in exts_to_prog:
        if file.endswith(ext):
            progs.add(exts_to_prog[ext])
            matched = True
    if not matched:
        sys.exit(
            "Unknown type of metrics file requested, for possible metrics files, see https://snakemake-wrappers.readthedocs.io/en/stable/wrappers/picard/collectmultiplemetrics.html"
        )

programs = " PROGRAM=" + " PROGRAM=".join(progs)

out = str(snakemake.wildcards.sample)  # as default
output_file = str(snakemake.output[0])
for ext in exts_to_prog:
    if output_file.endswith(ext):
        out = output_file[: -len(ext)]
        break

shell(
    "(picard CollectMultipleMetrics "
    "I={snakemake.input.bam} "
    "O={out} "
    "R={snakemake.input.ref} "
    "{extra} {programs} {java_opts}) {log}"
)
