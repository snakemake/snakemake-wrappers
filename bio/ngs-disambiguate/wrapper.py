"""Snakemake wrapper for ngs-disambiguate (from Astrazeneca)."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

prefix = (path.basename(snakemake.output[0])
          .replace(".ambiguousSpeciesA.bam", ""))
output_dir = path.dirname(snakemake.output[0])
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "ngs_disambiguate"
    " {extra}"
    " -o {output_dir}"
    " -s {prefix}"
    " -a {snakemake.params.algorithm}"
    " {snakemake.input.a}"
    " {snakemake.input.b}")
