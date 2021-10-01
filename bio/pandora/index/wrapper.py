"""Snakemake wrapper for indexing population reference graph (PRG) sequences with
pandora
"""

__author__ = "Michael Hall"
__copyright__ = "Copyright 2021, Michael Hall"
__email__ = "michael@mbh.sh"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=False)
options = snakemake.params.get("options", "")

shell("pandora index -t {snakemake.threads} {options} {snakemake.input} {log}")
