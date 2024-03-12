# coding: utf-8

"""Snakemake wrapper for pyTMB.py"""

__author__ = "Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__copyright__ = "Copyright 2024, Thibault Dayris"
__license__ = "MIT"

from re import sub
from snakemake import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

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
    "pyTMB.py {extra} "
    "{db_config} {var_config} {bed} "
    "--vcf {snakemake.input.vcf} "
    "> {snakemake.output.res} "
    "{log} "
)

# The export file is created in the execution directory
# with no option to control its prefix (other than the
# input vcf file prefix)
if out_vcf:
    prefix = sub("\.(v|b)cf(.gz)?", "", snakemake.input.vcf)
    log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
    shell("mv --verbose {prefix}_export.vcf {out_vcf} {log}")
