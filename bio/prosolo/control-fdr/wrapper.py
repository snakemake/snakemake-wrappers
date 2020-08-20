"""Snakemake wrapper for ProSolo FDR control"""

__author__ = "David Lähnemann"
__copyright__ = "Copyright 2020, David Lähnemann"
__email__ = "david.laehnemann@uni-due.de"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

os.system(
    f"( prosolo control-fdr"
    f" {snakemake.input}"
    f" --events {snakemake.params.events}"
    f" --var SNV"
    f" --fdr {snakemake.params.fdr}"
    f" --output {snakemake.output} )"
    f"{log} "
)
