# coding: utf-8

"""Snakemake wrapper for Sex.DetERRmine"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2024, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory

log = snakemake.log_fmt_shell(
    stdout=False,
    stderr=True,
    append=True,
)
extra = snakemake.params.get("extra", "")

shell("SampleCorrelation ")

