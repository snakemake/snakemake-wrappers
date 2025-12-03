"""Snakemake wrapper for falco."""

__author__ = "Yoann Pradat"
__copyright__ = "Copyright 2025, Yoann Pradat"
__email__ = "yoann.pradat@gustaveroussy.fr"
__license__ = "MIT"

import os
from tempfile import TemporaryDirectory
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

if len(snakemake.input) > 1:
    raise IOError("Got multiple input files, I don't know how to process them!")

# We use a temp dir to clean up intermediate files.
with TemporaryDirectory() as tempdir:
    shell(
        "falco"
        " --threads {snakemake.threads}"
        " {extra}"
        " --outdir {tempdir:q}"
        " {snakemake.input[0]:q}"
        " {log}"
    )

    html_path = os.path.join(tempdir, "fastqc_report.html")
    data_path = os.path.join(tempdir, "fastqc_data.txt")
    summ_path = os.path.join(tempdir, "summary.txt")

    shell("mv {html_path:q} {snakemake.output.html:q}")
    shell("mv {data_path:q} {snakemake.output.data:q}")
    shell("mv {summ_path:q} {snakemake.output.summ:q}")
