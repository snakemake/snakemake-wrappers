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


output_prefix = None
if snakemake.params.get("output_prefix"):
    # Make sure specified prefix matches listed output files
    output_prefix = snakemake.params.output_prefix
    for output in snakemake.output:
        output_file = os.path.basename(output)
        if not output_file.startswith(prefix):
            raise Exception(
                f"output file {output_file} doesn't start with the provided prefix {prefix}"
            )
else:
    expected_output_file_endings = [
        ".modelFinal.seq",
        ".cr.seg",
        ".af.igv.seg",
        ".cr.igv.seg",
        ".hets.tsv",
        ".modelBegin.cr.param",
        ".modelBegin.af.param",
        ".modelBegin.seg",
        ".modelFinal.af.param",
        ".modelFinal.cr.param",
    ]
    # Create prefix from listed output files
    for output in snakemake.output:
        output_file = os.path.basename(output)
        for output_extensions in expected_output_file_endings:
            if output_file.endswith(output_extensions):
                output_prefix = output_file.replace(output_extensions, "")
                break
        if output_prefix:
            break
    if not output_prefix:
        raise Exception(
            "Unable to extract prefix from listed files, expecting file(s) ending "
            f"with at least one of {expected_output_file_endings}"
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
        " --output-prefix {output_prefix}"
        " -O {output_folder}"
        " --tmp-dir {tmpdir}"
        " {extra}"
        " {log}"
    )

    for output in snakemake.output:
        filename = os.path.basename(output)
        outfile = os.path.join(output_folder, filename)
        shell("cp {outfile} {output}")
