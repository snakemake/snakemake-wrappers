__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smed"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


denoised_copy_ratios = ""
if snakemake.input.get("denoised_copy_ratios", None):
    denoised_copy_ratios = (
        f"--denoised-copy-ratios {snakemake.input.denoised_copy_ratios}"
    )

allelic_counts = ""
if snakemake.input.get("allelic_counts", None):
    allelic_counts = f"--allelic-counts {snakemake.input.allelic_counts}"

normal_allelic_counts = ""
if snakemake.input.get("normal_allelic_counts", None):
    matched_normal_allelic_counts = (
        f"--normal-allelic-counts {snakemake.inut.normal_allelic_counts}"
    )

segments = ""
if snakemake.input.get("segments", None):
    interval_list = f"--segments {snakemake.input.segments}"

if not allelic_counts and not denoised_copy_ratios:
    raise Exception(
        "wrapper input requires either 'allelic_counts' or 'denoise_copy_ratios' to be set"
    )

if normal_allelic_counts and not allelic_counts:
    raise Exception(
        "'allelica_counts' is required when 'normal-allelic-counts' is an input to the rule!"
    )

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)


with tempfile.TemporaryDirectory() as tmpdir:
    output_folder = os.path.join(tmpdir, "output_folder")
    shell(
        "gatk --java-options '{java_opts}' ModelSegments"
        " {segments}"
        " {denoised_copy_ratios}"
        " {allelic_counts}"
        " {normal_allelic_counts}"
        " --output-prefix temp_name__"
        " -O {output_folder}"
        " --tmp-dir {tmpdir}"
        " {extra}"
        " {log}"
    )

    created_files = {}
    # Find all created files
    for new_file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, new_file)
        if os.path.isfile(file_path):
            file_end = os.path.basename(file_path).split("__")[1]
            created_files[file_end] = file_path

    # Match expected output with found files
    for output in snakemake.output:
        file_found = False
        for file_ending in created_files:
            if output.endswith(file_ending):
                shell(f"cp {created_files[file_ending]} {output}")
                file_found = True
                break
        if not file_found:
            created_files_list = [f"{e}" for e in created_files]
            raise IOError(
                f"Could not create file {output}, possible files ends with {created_files_list}"
            )
