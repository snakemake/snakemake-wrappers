"""Snakemake wrapper for igv-reports."""

__author__ = "Johannes Köster"
__copyright__ = "Copyright 2019, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os

extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

tracks = snakemake.input.get("tracks", [])
if tracks:
    if isinstance(tracks, str):
        tracks = [tracks]
    tracks = "--tracks {}".format(" ".join(tracks))

os.system(
    f"create_report {extra} --standalone --output {snakemake.output[0]} {snakemake.input.vcf} {snakemake.input.fasta} {tracks} {log}"
)
