# coding: utf-8

"""Snakemake wrappers for sd"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2025, Thibault Dayris"
__license__ = "MIT"

from snakemake.shell import shell
from shlex import quote

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Snakemake does not treat empty strings as quotable arguments
# We use shlex.quote instead of `:q` syntax to force quotes around empty strings
before = quote(snakemake.params.get("before", ""))
after = quote(snakemake.params.get("after", ""))

# Since `sd` changes files in place,
# we use `cat` to disable this behavior
shell(
    "cat {snakemake.input:q} | "
    "sd {extra} {before} {after} "
    "> {snakemake.output:q} {log}"
)
