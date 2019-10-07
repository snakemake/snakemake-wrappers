"""Snakemake wrapper for sourmash compute."""

__author__ = "Lisa K. Johnson"
__copyright__ = "Copyright 2018, Lisa K. Johnson"
__email__ = "ljcohen@ucdavis.edu"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
scaled = snakemake.params.get("scaled", "1000")
k = snakemake.params.get("k", "31")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "sourmash compute --scaled {scaled} -k {k} {snakemake.input} -o {snakemake.output}"
    " {extra} {log}"
)
