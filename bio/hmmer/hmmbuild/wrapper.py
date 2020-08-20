"""Snakemake wrapper for hmmbuild"""

__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

import os
from os import path

extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    f" hmmbuild {extra} --cpu {snakemake.threads} "
    " {snakemake.output} {snakemake.input} {log} "
)
