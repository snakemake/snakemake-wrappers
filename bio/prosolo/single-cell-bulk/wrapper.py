"""Snakemake wrapper for ProSolo single-cell-bulk calling"""

__author__ = "David Lähnemann"
__copyright__ = "Copyright 2020, David Lähnemann"
__email__ = "david.laehnemann@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "( prosolo single-cell-bulk "
    "--omit-indels "
    "--candidates {input.candidates} "
    "--output {output} "
    "{input.single_cell} "
    "{input.bulk} "
    "{input.ref} ) "
    "{log} "
)
