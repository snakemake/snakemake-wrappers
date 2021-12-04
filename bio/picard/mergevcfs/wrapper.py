"""Snakemake wrapper for picard MergeSamFiles."""

__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


inputs = " ".join("INPUT={}".format(f) for f in snakemake.input.vcfs)
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

shell(
    "picard"
    " MergeVcfs"
    " {java_opts}"
    " {extra}"
    " {inputs}"
    " OUTPUT={snakemake.output[0]}"
    " {log}"
)
