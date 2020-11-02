"""Snakemake wrapper for picard MergeSamFiles."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params
java_opts = get_java_opts(snakemake)

inputs = " ".join("INPUT={}".format(in_) for in_ in snakemake.input)
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "picard"
    " MergeSamFiles"
    " {java_opts} {extra}"
    " {inputs}"
    " OUTPUT={snakemake.output[0]}"
    " {log}"
)
