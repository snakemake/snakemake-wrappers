"""Snakemake wrapper for Bismark methylation extractor tool: bismark_methylation_extractor."""
# https://github.com/FelixKrueger/Bismark/blob/master/bismark_methylation_extractor

__author__ = "Roman Chernyatchik"
__copyright__ = "Copyright (c) 2019 JetBrains"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"


import os
from snakemake.shell import shell

params_extra = snakemake.params.get("extra", "")
cmdline_args = ["bismark_methylation_extractor {params_extra}"]

# output dir
output_dir = snakemake.params.get("output_dir", "")
if output_dir:
    cmdline_args.append("-o {output_dir:q}")

# trimming options
trimming_options = [
    "ignore",  # meth_bias_r1_5end
    "ignore_3prime",  # meth_bias_r1_3end
    "ignore_r2",  # meth_bias_r2_5end
    "ignore_3prime_r2",  # meth_bias_r2_3end
]
for key in trimming_options:
    value = snakemake.params.get(key, None)
    if value:
        cmdline_args.append("--{} {}".format(key, value))

# Input
cmdline_args.append("{snakemake.input}")

# log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
cmdline_args.append("{log}")

# run
shell(" ".join(cmdline_args))

key2prefix_suffix = [
    ("mbias_report", ("", ".M-bias.txt")),
    ("mbias_r1", ("", ".M-bias_R1.png")),
    ("mbias_r2", ("", ".M-bias_R2.png")),
    ("splitting_report", ("", "_splitting_report.txt")),
    ("methylome_CpG_cov", ("", ".bismark.cov.gz")),
    ("methylome_CpG_mlevel_bedGraph", ("", ".bedGraph.gz")),
    ("read_base_meth_state_cpg", ("CpG_context_", ".txt.gz")),
    ("read_base_meth_state_chg", ("CHG_context_", ".txt.gz")),
    ("read_base_meth_state_chh", ("CHH_context_", ".txt.gz")),
]

log_append = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
for (key, (prefix, suffix)) in key2prefix_suffix:
    exp_path = snakemake.output.get(key, None)
    if exp_path:
        if len(snakemake.input) != 1:
            raise ValueError(
                "bismark/bismark_methylation_extractor: Error: only one BAM file is"
                " expected in input, but was <{}>".format(snakemake.input)
            )
        bam_file = snakemake.input[0]
        bam_name = os.path.basename(bam_file)
        bam_wo_ext = os.path.splitext(bam_name)[0]

        actual_path = os.path.join(output_dir, prefix + bam_wo_ext + suffix)
        if exp_path != actual_path:
            shell("mv {actual_path:q} {exp_path:q} {log_append}")
