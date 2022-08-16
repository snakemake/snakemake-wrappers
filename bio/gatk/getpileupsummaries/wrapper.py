#!/usr/bin/env python3
# coding: utf-8

"""Snakemake wrapper for GATK GetPileupSummaries"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2022, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

with tempfile.TemporaryDirectory() as tempdir:
    shell(
        "gatk GetPileupSummaries "
        "--java-options '{java_opts}' "
        "--input {snakemake.input.bam} "
        "--intervals {snakemake.input.intervals} "
        "--variant {snakemake.input.variants} "
        "--output {snakemake.output[0]} "
        "--tmp-dir {tempdir} "
        "{extra} "
        "{log} "
    )
