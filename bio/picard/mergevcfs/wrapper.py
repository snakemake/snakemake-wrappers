"""Snakemake wrapper for picard MergeSamFiles."""

__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os


inputs = " ".join("INPUT={}".format(f) for f in snakemake.input.vcfs)
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

os.system(
    f"picard"
    f" MergeVcfs"
    f" {extra}"
    f" {inputs}"
    f" OUTPUT={snakemake.output[0]}"
    f" {log}"
)
