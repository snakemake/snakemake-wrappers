"""Snakemake wrapper for ProSolo single-cell-bulk calling"""

__author__ = "David Lähnemann"
__copyright__ = "Copyright 2020, David Lähnemann"
__email__ = "david.laehnemann@uni-due.de"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

os.system(
    f"( prosolo single-cell-bulk "
    f"--omit-indels "
    f" {snakemake.params.extra} "
    f"--candidates {snakemake.input.candidates} "
    f"--output {snakemake.output} "
    f"{snakemake.input.single_cell} "
    f"{snakemake.input.bulk} "
    f"{snakemake.input.ref} ) "
    f"{log} "
)
