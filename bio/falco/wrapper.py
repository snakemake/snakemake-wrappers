"""Snakemake wrapper for falco."""

__author__ = "Yoann Pradat"
__copyright__ = "Copyright 2025, Yoann Pradat"
__email__ = "yoann.pradat@gustaveroussy.fr"
__license__ = "MIT"

import os
from tempfile import TemporaryDirectory
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import move_files

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

if len(snakemake.input) > 1:
    raise IOError("Got multiple input files, I don't know how to process them!")

# We use a temp dir to clean up intermediate files.
with TemporaryDirectory() as tempdir:
mapping = {"html": Path(tmpdir) / "fastqc_report.html",
           "data": Path(tmpdir) / "fastqc_data.txt",
           "summ": Path(tmpdir) / "summary.txt",}
    shell(
        "falco"
        " --threads {snakemake.threads}"
        " {extra}"
        " --outdir {tempdir:q}"
        " {snakemake.input[0]:q}"
        " {log}"
    )

    log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
    for move_cmd in move_files(snakemake, mapping):
        shell("{move_cmd} {log}")
