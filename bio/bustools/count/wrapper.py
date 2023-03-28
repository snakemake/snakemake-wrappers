#!/usr/bin/env python3
# coding: utf-8

"""Snakemake wrapper for bustools count"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2022, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from os.path import commonprefix

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Get IO files and prefixes
bus_files = snakemake.input["bus"]
if isinstance(bus_files, list):
    bus_files = " ".join(bus_files)

out_prefix = commonprefix(snakemake.output)[:-1]

# Fill extra parameters if needed
extra = snakemake.params.get("extra", "")
if any(outfile.endswith(".hist.txt") for outfile in snakemake.output):
    if "--hist" not in extra:
        extra += " --hist"

if any(outfile.endswith(".genes.txt") for outfile in snakemake.output):
    if "--genecounts" not in extra:
        extra += " --genecounts"

shell(
    "bustools count {extra} "
    "--output {out_prefix} "
    "--genemap {snakemake.input.genemap} "
    "--ecmap {snakemake.input.ecmap} "
    "--txnames {snakemake.input.txnames} "
    "{bus_files} "
    "{log}"
)
