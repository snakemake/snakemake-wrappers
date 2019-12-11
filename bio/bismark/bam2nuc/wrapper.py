"""Snakemake wrapper for bam2nuc tool that calculates mono- and di-nucleotide coverage of the reads and compares them with average genomic sequence
composition."""
# https://github.com/FelixKrueger/Bismark/blob/master/bam2nuc

__author__ = "Roman Chernyatchik"
__copyright__ = "Copyright (c) 2019 JetBrains"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"

import os

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
cmdline_args = ["bam2nuc {extra}"]

genome_fa = snakemake.input.get("genome_fa", None)
if not genome_fa:
    raise ValueError("bismark/bam2nuc: Error 'genome_fa' input not specified.")
genome_folder = os.path.dirname(genome_fa)
cmdline_args.append("--genome_folder {genome_folder:q}")


bam = snakemake.input.get("bam", None)
if bam:
    cmdline_args.append("{bam}")
    bams = bam if isinstance(bam, list) else [bam]

    report = snakemake.output.get("report", None)
    if not report:
        raise ValueError("bismark/bam2nuc: Error 'report' output isn't specified.")

    reports = report if isinstance(report, list) else [report]
    if len(reports) != len(bams):
        raise ValueError(
            "bismark/bam2nuc: Error number of paths in output:report ({} files)"
            " should be same as in input:bam ({} files).".format(
                len(reports), len(bams)
            )
        )
    output_dir = os.path.dirname(reports[0])
    if any(output_dir != os.path.dirname(p) for p in reports):
        raise ValueError(
            "bismark/bam2nuc: Error all reports should be in same directory:"
            " {}".format(output_dir)
        )
    if output_dir:
        cmdline_args.append("--dir {output_dir:q}")
else:
    cmdline_args.append("--genomic_composition_only")

# log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
cmdline_args.append("{log}")

# run
shell(" ".join(cmdline_args))


# Move outputs into proper position.
if bam:
    log_append = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

    expected_2_actual_paths = []
    for bam_path, report_path in zip(bams, reports):
        bam_name = os.path.basename(bam_path)
        bam_basename = os.path.splitext(bam_name)[0]
        expected_2_actual_paths.append(
            (
                report_path,
                os.path.join(
                    output_dir, "{}.nucleotide_stats.txt".format(bam_basename)
                ),
            )
        )

    for (exp_path, actual_path) in expected_2_actual_paths:
        if exp_path and (exp_path != actual_path):
            shell("mv {actual_path:q} {exp_path:q} {log_append}")
