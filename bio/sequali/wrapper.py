"""Snakemake wrapper for Sequali."""

__author__ = "Artur Gomes"
__copyright__ = "Copyright 2026, Artur Gomes"
__email__ = "arafaelogomes@gmail.com"
__license__ = "MIT"

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

images_zip = snakemake.output.get("images_zip", "")
if images_zip:
    images_zip = f"--images-zip {images_zip}"

adapter_file = snakemake.input.get("adapter_file", "")
if adapter_file:
    adapter_file = f"--adapter-file {adapter_file}"

shell(
    "sequali"
    " --threads {snakemake.threads}"
    " --json {snakemake.output.json:q}"
    " --html {snakemake.output.html:q}"
    " {images_zip}"
    " {adapter_file}"
    " {extra}"
    " {reads:q}"
    " {log}"
)
