"""Snakemake wrapper for Sequali."""

__author__ = "Artur Gomes"
__copyright__ = "Copyright 2026, Artur Gomes"
__email__ = "arafaelogomes@gmail.com"
__license__ = "MIT"

import shlex

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

reads = snakemake.input.sample
if isinstance(reads, str):
    reads = [reads]

assert len(reads) in {
    1,
    2,
}, "input->sample must have 1 (single-end) or 2 (paired-end) elements."

images_zip = snakemake.output.get("images_zip")
images_zip_arg = f"--images-zip {shlex.quote(images_zip)}" if images_zip else ""

adapter_file = snakemake.input.get("adapter_file")
adapter_file_arg = f"--adapter-file {shlex.quote(adapter_file)}" if adapter_file else ""

shell(
    "sequali"
    " --threads {snakemake.threads}"
    " --json {snakemake.output.json:q}"
    " --html {snakemake.output.html:q}"
    " {images_zip_arg}"
    " {adapter_file_arg}"
    " {extra}"
    " {reads:q}"
    " {log}"
)
