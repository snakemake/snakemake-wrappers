# coding: utf-8

"""Snakemake wrapper for NGS-bits SampleSimilarity"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2024, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(
    stdout=True,
    stderr=True,
)
extra = snakemake.params.get("extra", "")
ref = snakemake.input.get("ref")
if ref:
    extra += f" -ref {ref:q}"

roi = snakemake.input.get("regions")
if roi:
    extra += f" -roi {roi:q}"

input_files = snakemake.input.get("samples")
if all(str(i).endswith((".vcf", ".vcf.gz")) for i in input_files):
    extra += " -mode vcf"
elif all(str(i).endswith((".sam", ".bam", ".cram")) for i in input_files):
    extra += " -mode bam"
else:
    extra += " -mode gsvar"

shell(
    "SampleSimilarity"
    " -in {input_files}"
    " {extra}"
    " -out {snakemake.output:q}"
    " {log}"
)
