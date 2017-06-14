"""Snakemake wrapper for fastqc."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

output_dir = path.dirname(snakemake.output.html)

shell("fastqc {snakemake.params} --quiet "
      "--outdir {output_dir} {snakemake.input[0]}")
