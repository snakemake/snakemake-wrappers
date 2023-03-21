__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


from os import path
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra_params = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

bam_input = snakemake.input[0]

family_sizes = snakemake.output.family_sizes
duplex_family_sizes = snakemake.output.duplex_family_sizes
duplex_yield_metrics = snakemake.output.duplex_yield_metrics
umi_counts = snakemake.output.umi_counts
duplex_qc = snakemake.output.duplex_qc
duplex_umi_counts = snakemake.output.get("duplex_umi_counts", None)

file_path = str(path.dirname(family_sizes))
name = str(path.basename(family_sizes)).split(".")[0]
path_name_prefix = str(path.join(file_path, name))

if not family_sizes == path_name_prefix + ".family_sizes.txt":
    raise Exception(
        "Unexpected family_sizes path/name format, expected {}, got {}.".format(
            path_name_prefix + ".family_sizes.txt", family_sizes
        )
    )
if not duplex_family_sizes == path_name_prefix + ".duplex_family_sizes.txt":
    raise Exception(
        "Unexpected duplex_family_sizes path/name format, expected {}, got {}. Note that dirname will be extracted from family_sizes variable.".format(
            path_name_prefix + ".duplex_family_sizes.txt", duplex_family_sizes
        )
    )
if not duplex_yield_metrics == path_name_prefix + ".duplex_yield_metrics.txt":
    raise Exception(
        "Unexpected duplex_yield_metrics path/name format, expected {}, got {}. Note that dirname will be extracted from family_sizes variable.".format(
            path_name_prefix + ".duplex_yield_metrics.txt", duplex_yield_metrics
        )
    )
if not umi_counts == path_name_prefix + ".umi_counts.txt":
    raise Exception(
        "Unexpected umi_counts path/name format, expected {}, got {}. Note that dirname will be extracted from family_sizes variable.".format(
            path_name_prefix + ".umi_counts.txt", umi_counts
        )
    )
if not duplex_qc == path_name_prefix + ".duplex_qc.pdf":
    raise Exception(
        "Unexpected duplex_qc path/name format, expected {}, got {}. Note that dirname will be extracted from family_sizes variable.".format(
            path_name_prefix + ".duplex_qc.pdf", duplex_qc
        )
    )
if (
    duplex_umi_counts is not None
    and not duplex_umi_counts == path_name_prefix + ".duplex_umi_counts.txt"
):
    raise Exception(
        "Unexpected duplex_umi_counts path/name format, expected {}, got {}. Note that dirname will be extracted from family_sizes variable.".format(
            path_name_prefix + ".duplex_umi_counts.txt", duplex_umi_counts
        )
    )

duplex_umi_counts_flag = ""
if duplex_umi_counts is not None:
    duplex_umi_counts_flag = "-u "

if not isinstance(bam_input, str) and len(snakemake.input) != 1:
    raise ValueError("Input bam should be one bam file: " + str(bam_input) + "!")

shell(
    "fgbio {java_opts} CollectDuplexSeqMetrics"
    " -i {bam_input}"
    " -o {path_name_prefix}"
    " {duplex_umi_counts_flag}"
    " {extra_params}"
    " {log}"
)
