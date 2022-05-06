"""Snakemake wrapper for picard RevertSam."""

__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2018, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard RevertSam"
        " {java_opts} {extra}"
        " --INPUT {snakemake.input[0]}"
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {snakemake.output[0]}"
        " {log}"
    )
