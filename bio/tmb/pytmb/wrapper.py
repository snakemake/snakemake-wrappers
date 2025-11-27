# coding: utf-8

"""Snakemake wrapper for pyTMB.py"""

__author__ = "Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__copyright__ = "Copyright 2024, Thibault Dayris"
__license__ = "MIT"

from pathlib import Path
from snakemake import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True, append=True)
extra = snakemake.params.get("extra", "")

db_config = snakemake.input.get("db_config", "")
if db_config:
    db_config = f"--dbConfig {db_config}"

var_config = snakemake.input.get("var_config", "")
if var_config:
    var_config = f"--varConfig {var_config}"

bed = snakemake.input.get("bed", "")
if bed:
    bed = f"--bed {bed}"

out_vcf = snakemake.output.get("vcf", "")
if out_vcf:
    extra += " --export"

shell(
    "pyTMB.py"
    " --vcf {snakemake.input.vcf}"
    " {db_config}"
    " {var_config}"
    " {bed}"
    " {extra}"
    " > {snakemake.output.res}"
    " {log}"
)

# Moving the optional exported VCF file
if out_vcf:
    prefix = Path(snakemake.input.vcf.removesuffix(".gz")).with_suffix("").name
    shell("mv --verbose {prefix}_export.vcf.gz {out_vcf} {log}")
