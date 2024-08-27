# coding: utf-8

"""Snakemake wrapper to run RSeQC bam_stat.py"""

__author__ = "Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__copyright__ = "Copyright 2024, Thibault Dayris"
__license__ = "MIT"

from snakemake import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "bam_stat.py "
    "--input-file {snakemake.input[0]} "
    "> {snakemake.output} {log}"
)
