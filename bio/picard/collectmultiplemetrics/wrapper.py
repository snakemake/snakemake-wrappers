__author__ = "David Laehnemann, Antonie Vietor"
__copyright__ = "Copyright 2020, David Laehnemann, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

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


# Select programs to run from output files
progs = set()
for file in snakemake.output:
    matched = False
    for ext in exts_to_prog:
        if file.endswith(ext):
            progs.add(exts_to_prog[ext])
            matched = True
    if not matched:
        raise ValueError(
            "Unknown type of metrics file requested, for possible metrics files, see https://snakemake-wrappers.readthedocs.io/en/stable/wrappers/picard/collectmultiplemetrics.html"
        )

programs = "--PROGRAM null --PROGRAM " + " --PROGRAM ".join(progs)


# Infer common output prefix
output_file = str(snakemake.output[0])
for ext in exts_to_prog:
    if output_file.endswith(ext):
        out = output_file[: -len(ext)]
        break


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard CollectMultipleMetrics"
        " {java_opts} {extra}"
        " --INPUT {snakemake.input.bam}"
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {out}"
        " --REFERENCE_SEQUENCE {snakemake.input.ref}"
        " {programs}"
        " {log}"
    )


# Under some circumstances, some picard programs might not produce an output (https://github.com/snakemake/snakemake-wrappers/issues/357). To avoid snakemake errors, the output files of those programs are created empty (if they do not exist).
for ext in [
    ext for ext, prog in exts_to_prog.items() if prog in ["CollectInsertSizeMetrics"]
]:
    for file in snakemake.output:
        if file.endswith(ext) and not Path(file).is_file():
            Path(file).touch()
