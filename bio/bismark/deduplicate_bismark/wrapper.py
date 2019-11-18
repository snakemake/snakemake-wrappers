"""Snakemake wrapper for Bismark aligned reads deduplication using deduplicate_bismark."""
# https://github.com/FelixKrueger/Bismark/blob/master/deduplicate_bismark

__author__ = "Roman Chernyatchik"
__copyright__ = "Copyright (c) 2019 JetBrains"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"

import os
from snakemake.shell import shell

bam_path = snakemake.output.get("bam", None)
report_path = snakemake.output.get("report", None)
if not bam_path or not report_path:
    raise ValueError(
        "bismark/deduplicate_bismark: Please specify both 'bam=..' and 'report=..' paths in output section"
    )

output_dir = os.path.dirname(bam_path)
if output_dir != os.path.dirname(report_path):
    raise ValueError(
        "bismark/deduplicate_bismark: BAM and Report files expected to have the same parent directory"
        " but was {} and {}".format(bam_path, report_path)
    )

arg_output_dir = "--output_dir '{}'".format(output_dir) if output_dir else ""
arg_multiple = "--multiple" if len(snakemake.input) > 1 else ""

params_extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
log_append = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
shell(
    "deduplicate_bismark {params_extra} --bam {arg_multiple}"
    " {arg_output_dir} {snakemake.input} {log}"
)

# Move outputs into proper position.
fst_input_filename = os.path.basename(snakemake.input[0])
fst_input_basename = os.path.splitext(fst_input_filename)[0]
prefix = os.path.join(output_dir, fst_input_basename)

deduplicated_bam_actual_name = prefix + ".deduplicated.bam"
if arg_multiple:
    # bismark does it exactly like this:
    deduplicated_bam_actual_name = deduplicated_bam_actual_name.replace(
        "deduplicated", "multiple.deduplicated", 1
    )

expected_2_actual_paths = [
    (bam_path, deduplicated_bam_actual_name),
    (
        report_path,
        prefix + (".multiple" if arg_multiple else "") + ".deduplication_report.txt",
    ),
]
for (exp_path, actual_path) in expected_2_actual_paths:
    if exp_path and (exp_path != actual_path):
        shell("mv {actual_path:q} {exp_path:q} {log_append}")
