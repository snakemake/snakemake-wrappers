"""Snakemake wrapper for jackhmmer"""

__author__ = "Thomas Mulvaney, N. Tessa Pierce"
__copyright__ = "Copyright 2025, Thomas Mulvaney, N. Tessa Pierce"
__email__ = "mulvaney@mailbox.org"
__license__ = "MIT"

from os import path
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Output must be set even if its not desired.  Default to '/dev/null'
out_cmd = f" -o {snakemake.output.get('summary', '/dev/null')}"

if snakemake.output.get("tblout") is not None:
    out_cmd += f" --tblout {snakemake.output.get('hits_tbl')}"

if snakemake.output.get("domtblout") is not None:
    out_cmd += f" --domtblout {snakemake.output.get('dom_tbl')}"

if snakemake.output.get("alignment_hits") is not None:
    out_cmd += f" -A {snakemake.output.get('hits_aln')}"

shell(
    "jackhmmer --cpu {snakemake.threads}"
    " {extra}"
    " {out_cmd}"
    " {snakemake.input.query}"
    " {snakemake.input.db}"
    " {log}"
)
