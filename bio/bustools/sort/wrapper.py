#!/usr/bin/env python3
# coding: utf-8

"""Snakemake wrapper for bustools sort"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2022, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory
from snakemake_wrapper_utils.snakemake import get_mem

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

bus_files = snakemake.input
if isinstance(bus_files, list):
    bus_files = " ".join(bus_files)

mem = get_mem(snakemake, "MiB")


with TemporaryDirectory() as tempdir:
    shell(
        "bustools sort "
        "--memory {mem} "
        "--temp {tempdir} "
        "--threads {snakemake.threads} "
        "--output {snakemake.output[0]} "
        "{bus_files} "
        "{log}"
    )
