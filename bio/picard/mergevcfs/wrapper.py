"""Snakemake wrapper for picard MergeSamFiles."""

__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


from snakemake.shell import shell


inputs = " ".join("INPUT={}".format(f) for f in snakemake.input)
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

shell(
    "picard"
    " MergeVcfs"
    " {extra}"
    " {inputs}"
    " OUTPUT={snakemake.output[0]}"
    " {log}"
)
