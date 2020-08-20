"""Snakemake wrapper for Bismark indexes preparing using bismark_genome_preparation."""
# https://github.com/FelixKrueger/Bismark/blob/master/bismark_genome_preparation

__author__ = "Roman Chernyatchik"
__copyright__ = "Copyright (c) 2019 JetBrains"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"


import os
from os import path

input_dir = path.dirname(snakemake.input[0])

params_extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

os.system(
    f"bismark_genome_preparation --verbose --bowtie2 {params_extra} {input_dir} {log}"
)
