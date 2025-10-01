# coding: utf-8

"""Snakemake wrapper for NGS-bits SampleAncestry"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2024, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(
    stdout=False,
    stderr=True,
)
extra = snakemake.params.get("extra", "")

shell(
    "SampleAncestry {extra}"
    " -in {snakemake.input}"
    " -out {snakemake.output:q}"
    " {log}"
)
