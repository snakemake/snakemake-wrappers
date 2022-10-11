#!/usr/bin/env python3
# coding: utf-8

"""Snakemake wrapper for GATK4 LearnReadOrientationModel"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2022, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

f1r2 = "--input "
if isinstance(snakemake.input["f1r2"], list):
    # Case user provided a list of archives
    f1r2 += "--input ".join(snakemake.input["f1r2"])
else:
    # Case user provided a single archive as a string
    f1r2 += snakemake.input["f1r2"]


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' LearnReadOrientationModel"  # Tool and its subprocess
        " {f1r2}"  # Path to input mapping file
        " {extra}"  # Extra parameters
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output[0]}"  # Path to output vcf file
        " {log}"  # Logging behaviour
    )
