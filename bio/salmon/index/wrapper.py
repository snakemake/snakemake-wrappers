"""Snakemake wrapper for Salmon Index."""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2018, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

os.system(
    f"salmon index -t {snakemake.input} -i {snakemake.output} "
    f" --threads {snakemake.threads} {extra} {log}"
)
