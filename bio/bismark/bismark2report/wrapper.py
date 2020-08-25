"""Snakemake wrapper to generate graphical HTML report from Bismark reports."""
# https://github.com/FelixKrueger/Bismark/blob/master/bismark2report

__author__ = "Roman Chernyatchik"
__copyright__ = "Copyright (c) 2019 JetBrains"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"

import os


def answer2bool(v):
    return str(v).lower() in ("yes", "true", "t", "1")


extra = snakemake.params.get("extra", "")
cmds = [f"bismark2report {extra}"]

# output
html_file = snakemake.output.get("html", "")
output_dir = snakemake.output.get("html_dir", None)
if output_dir is None:
    if html_file:
        output_dir = os.path.dirname(html_file)
else:
    if html_file:
        raise ValueError(
            "bismark/bismark2report: Choose one: 'html=...' for a single dir or 'html_dir=...' for batch processing."
        )

if output_dir is None:
    raise ValueError(
        "bismark/bismark2report: Output file or directory not specified. "
        "Use 'html=...' for a single dir or 'html_dir=...' for batch "
        "processing."
    )

if output_dir:
    cmds.append(f"--dir {output_dir}")

if html_file:
    html_file_name = os.path.basename(html_file)
    cmds.append(f"--output {html_file_name}")

# reports
reports = [
    "alignment_report",
    "dedup_report",
    "splitting_report",
    "mbias_report",
    "nucleotide_report",
]
skip_optional_reports = answer2bool(
    snakemake.params.get("skip_optional_reports", False)
)

for report_name in reports:
    path = snakemake.input.get(report_name, "")
    if path:
        cmds.append("--%s %s" % (report_name, path))
    elif skip_optional_reports:
        cmds.append("--%s 'none'" % report_name)

# log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
cmds.append(f"{log}")

# run shell command:
os.system(" ".join(cmds))
