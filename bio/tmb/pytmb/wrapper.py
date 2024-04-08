# coding: utf-8

"""Snakemake wrapper for pyTMB.py"""

__author__ = "Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__copyright__ = "Copyright 2024, Thibault Dayris"
__license__ = "MIT"

from os.path import basename
from re import sub
from snakemake import shell
from tempfile import TemporaryDirectory


extra = snakemake.params.get("extra", "")
ln_extra = "--symbolic --force --relative --verbose"

out_vcf = snakemake.output.get("vcf", "")
if out_vcf:
    extra += " --export"

# pyTMB creates an exported VCF file which name/prefix
# is predictible, but not editable. It is based on input
# vcf file name.
# It was chosen to handle this issue in the wrapper itself,
# rather than expecting user to define `shadow` directive
# in the Snakemake rule.
with TemporaryDirectory() as tempdir:
    # Linking all input files in the creates temporary directory
    vcf_link_path = f"{tempdir}/{basename(snakemake.input.vcf)}"
    log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
    shell("ln {ln_extra} {snakemake.input.vcf} {vcf_link_path} {log}")

    db_config = snakemake.input.get("db_config", "")
    if db_config:
        db_link_path = f"{tempdir}/{basename(db_config)}"
        shell("ln {ln_extra} {db_config} {db_link_path} {log}")
        db_config = f"--dbConfig {db_link_path}"

    var_config = snakemake.input.get("var_config", "")
    if var_config:
        var_link_path = f"{tempdir}/{basename(var_config)}"
        shell("ln {ln_extra} {var_config} {var_link_path} {log}")
        var_config = f"--varConfig {var_link_path}"

    bed = snakemake.input.get("bed", "")
    if bed:
        bed_link_path = f"{tempdir}/{basename(bed)}"
        shell("ln {ln_extra} {bed} {bed_link_path} {log}")
        bed = f"--bed {bed_link_path}"

    res_link_name = f"{tempdir}/{basename(snakemake.output.res)}"

    # Running pyTMB on symlinked files, after moving
    # into the temporary directory in order to let
    # the exported VCF file be there.
    # The exported VCF file is created in working directory.
    log = snakemake.log_fmt_shell(stdout=False, stderr=True, append=True)
    shell(
        "cd {tempdir} && "
        "pyTMB.py {extra} "
        "{db_config} {var_config} {bed} "
        "--vcf {vcf_link_path} "
        "> {res_link_name} "
        "{log} && "
        "cd - "
    )

    # Moving the main result file
    log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
    shell("mv --verbose {res_link_name} {snakemake.output.res} {log}")

    # Moving the optional exported VCF file
    if out_vcf:
        prefix = sub("\.(v|b)cf(.gz)?", "", f"{vcf_link_path}")
        shell("mv --verbose {prefix}_export.vcf {out_vcf} {log}")
