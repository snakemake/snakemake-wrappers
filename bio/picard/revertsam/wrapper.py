"""Snakemake wrapper for picard RevertSam."""

__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2018, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "picard"
    " RevertSam"
    " {java_opts}"
    " {extra}"
    " INPUT={snakemake.input[0]}"
    " OUTPUT={snakemake.output[0]}"
    " {log}"
)
