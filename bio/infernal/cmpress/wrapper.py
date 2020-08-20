"""Snakemake wrapper for Infernal CMpress"""

__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

import os
from os import path

extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# -F enables overwrite of old (otherwise cmpress will fail if old versions exist)
os.system(f"cmpress -F {snakemake.input} {log}")
