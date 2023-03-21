"""Snakemake wrapper for aligning methylation BS-Seq data using Bismark."""
# https://github.com/FelixKrueger/Bismark/blob/master/bismark

__author__ = "Roman Chernyatchik"
__copyright__ = "Copyright (c) 2019 JetBrains"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"

import os

from snakemake.shell import shell
from tempfile import TemporaryDirectory


def basename_without_ext(file_path):
    """Returns basename of file path, without the file extension."""

    base = os.path.basename(file_path)

    split_ind = 2 if base.endswith(".gz") else 1
    base = ".".join(base.split(".")[:-split_ind])

    return base


extra = snakemake.params.get("extra", "")
cmdline_args = ["bismark {extra} --bowtie2"]

outdir = os.path.dirname(snakemake.output.bam)
if outdir:
    cmdline_args.append("--output_dir {outdir}")

genome_indexes_dir = os.path.dirname(snakemake.input.bismark_indexes_dir)
cmdline_args.append("{genome_indexes_dir}")

if not snakemake.output.get("bam", None):
    raise ValueError("bismark/bismark: Error 'bam' output file isn't specified.")
if not snakemake.output.get("report", None):
    raise ValueError("bismark/bismark: Error 'report' output file isn't specified.")

# basename
if snakemake.params.get("basename", None):
    cmdline_args.append("--basename {snakemake.params.basename:q}")
    basename = snakemake.params.basename
else:
    basename = None

# reads input
single_end_mode = snakemake.input.get("fq", None)
if single_end_mode:
    # for SE data, you only have to specify read1 input by -i or --in1, and
    # specify read1 output by -o or --out1.
    cmdline_args.append("--se {snakemake.input.fq:q}")
    mode_prefix = "se"
    if basename is None:
        basename = basename_without_ext(snakemake.input.fq)
else:
    # for PE data, you should also specify read2 input by -I or --in2, and
    # specify read2 output by -O or --out2.
    cmdline_args.append("-1 {snakemake.input.fq_1:q} -2 {snakemake.input.fq_2:q}")
    mode_prefix = "pe"

    if basename is None:
        # default basename
        basename = basename_without_ext(snakemake.input.fq_1) + "_bismark_bt2"

# log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
cmdline_args.append("{log}")

# run
shell(" ".join(cmdline_args))

# Move outputs into proper position.
expected_2_actual_paths = [
    (
        snakemake.output.bam,
        os.path.join(
            outdir, "{}{}.bam".format(basename, "" if single_end_mode else "_pe")
        ),
    ),
    (
        snakemake.output.report,
        os.path.join(
            outdir,
            "{}_{}_report.txt".format(basename, "SE" if single_end_mode else "PE"),
        ),
    ),
    (
        snakemake.output.get("nucleotide_stats", None),
        os.path.join(
            outdir,
            "{}{}.nucleotide_stats.txt".format(
                basename, "" if single_end_mode else "_pe"
            ),
        ),
    ),
]
log_append = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
for exp_path, actual_path in expected_2_actual_paths:
    if exp_path and (exp_path != actual_path):
        shell("mv {actual_path:q} {exp_path:q} {log_append}")
