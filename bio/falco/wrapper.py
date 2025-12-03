"""Snakemake wrapper for falco."""

__author__ = "Yoann Pradat"
__copyright__ = "Copyright 2025, Yoann Pradat"
__email__ = "yoann.pradat@gustaveroussy.fr"
__license__ = "MIT"

import os
import re
from tempfile import TemporaryDirectory
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

if len(snakemake.input) > 1:
    raise IOError("Got multiple input files, I don't know how to process them!")

# Output directory
output_dir_out = snakemake.output.get("dir", "")
output_dir_param = snakemake.params.get("output_dir", "")
if output_dir_out and output_dir_param:
    raise ValueError(
        "You provided values for output_dir via snakemake output and parameters. Choose one."
    )
else:
    if output_dir_out:
        output_dir_user = output_dir_out
    else:
        output_dir_user = output_dir_param

# Run falco.
# We use a temp dir to clean up intermediate files.
with TemporaryDirectory() as tempdir:
    # if the user did not specify an output directory, use temporary directory
    if not output_dir_user:
        output_dir_algo = os.path.join(tempdir, "falco")
    else:
        output_dir_algo = output_dir_user

    shell(
        "falco"
        " --threads {snakemake.threads}"
        " {extra}"
        " --outdir {output_dir_algo:q}"
        " {snakemake.input[0]:q}"
        " {log}"
    )

    # If the user did not specify an output directory in the snakemake outputs, move individual files
    # to the locations specified by the user
    if output_dir_out == "":
        html_path = os.path.join(output_dir_algo, "fastqc_report.html")
        data_path = os.path.join(output_dir_algo, "fastqc_data.txt")
        summ_path = os.path.join(output_dir_algo, "summary.txt")

        if snakemake.output.html != html_path:
            shell("mv {html_path:q} {snakemake.output.html:q}")

        if snakemake.output.data != data_path:
            shell("mv {data_path:q} {snakemake.output.data:q}")

        if snakemake.output.summ != summ_path:
            shell("mv {summ_path:q} {snakemake.output.summ:q}")
