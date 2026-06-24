# coding: utf-8

"""Snakemake wrappers for sd"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2025, Thibault Dayris"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Since `sd` changes files inplace,
# we use `cat` to disable this behavior
shell(
    "cat {snakemake.input} | "
    "sd {extra} {snakemake.params.before:q} {snakemake.params.after:q} "
    "> {snakemake.output} {log}"
)
