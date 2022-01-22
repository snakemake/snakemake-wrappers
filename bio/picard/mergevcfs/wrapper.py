"""Snakemake wrapper for picard MergeSamFiles."""

__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


inputs = " ".join("--INPUT {}".format(f) for f in snakemake.input.vcfs)
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard MergeVcfs"
        " {java_opts} {extra}"
        " {inputs}"
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {snakemake.output[0]}"
        " {log}"
    )
