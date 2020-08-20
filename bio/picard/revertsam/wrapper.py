"""Snakemake wrapper for picard RevertSam."""

__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2018, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


import os

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    f"picard"
    f" RevertSam"
    f" {extra}"
    f" INPUT={snakemake.input[0]}"
    f" OUTPUT={snakemake.output[0]}"
    f" {log}"
)
