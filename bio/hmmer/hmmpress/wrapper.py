"""Snakemake wrapper for hmmpress"""

__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

import os
from os import path

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# -f Force; overwrites any previous hmmpress-ed datafiles. The default is to bitch about any existing files and ask you to delete them first.

os.system(f"hmmpress -f {snakemake.input} {log}")
