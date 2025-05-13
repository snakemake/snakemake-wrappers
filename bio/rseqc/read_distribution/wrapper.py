# coding: utf-8

__author__ = "Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__copyright__ = "Copyright 2024, Thibault Dayris"
__license__ = "MIT"

from snakemake import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "read_distribution.py "
    "--input-file {snakemake.input.aln} "
    "--refgene {snakemake.input.refgene} "
    "> {snakemake.output} {log} "
)
