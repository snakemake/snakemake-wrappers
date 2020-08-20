"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


import os
from os import path


input_dirs = set(path.dirname(fp) for fp in snakemake.input)
output_dir = path.dirname(snakemake.output[0])
output_name = path.basename(snakemake.output[0])
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

os.system(
    f"multiqc"
    f" {snakemake.params}"
    f" --force"
    f" -o {output_dir}"
    f" -n {output_name}"
    f" {input_dirs}"
    f" {log}"
)
