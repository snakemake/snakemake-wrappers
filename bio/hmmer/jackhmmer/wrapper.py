"""Snakemake wrapper for jackhmmer"""

__author__ = "Thomas Mulvaney, N. Tessa Pierce"
__copyright__ = "Copyright 2025, Thomas Mulvaney, N. Tessa Pierce"
__email__ = "mulvaney@mailbox.org"
__license__ = "MIT"

from os import path
from snakemake.shell import shell


# Output must be set even if its not desired.  Default to '/dev/null'
out_cmd = (f" -o {snakemake.output.get('outfile', '/dev/null')}",)

if snakemake.output.get("tblout") is not None:
    out_cmd += (f" --tblout {snakemake.output.get('tblout')}",)

if snakemake.output.get("domtblout") is not None:
    out_cmd += (f" --domtblout {snakemake.output.get('domtblout')}",)

if snakemake.output.get("alignment_hits") is not None:
    out_cmd += (f" -A {snakemake.output.get('alignment_hits')}",)

extra_flags = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    " jackhmmer --cpu {snakemake.threads} "
    " {out_cmd} {extra_flags} "
    " {snakemake.input.query} {snakemake.input.db} {log}"
)
