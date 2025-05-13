#!/usr/bin/env python3
# coding: utf-8

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

# Consider user input datasets
input_data = ""
if all(key in snakemake.input.keys() for key in ["tumor", "normal"]):
    input_data = f" --snp-tumour {snakemake.input.tumor} --snp-normal {snakemake.input.normal}  --snp-vcf {snakemake.input.vcf} "
elif "pileup" in snakemake.input.keys():
    input_data = f" --pileup {snakemake.input.pileup} --snp-vcf {snakemake.input.vcf} "
else:
    raise KeyError(
        "Either provide both `tumor` *and* `normal` bam files, "
        "or a unique `pileup` file."
    )

with TemporaryDirectory() as tempdir:
    prefix = f"{tempdir}/facets_output"

    # Run cnv_facets
    shell(
        "cnv_facets.R "
        "{extra} "
        "--snp-nprocs {snakemake.threads} "
        "{input_data} "
        "-o {prefix} "
        "{log}"
    )

    # Allow user to define all output files
    if snakemake.output.get("vcf"):
        shell("mv --verbose {prefix}.vcf.gz {snakemake.output.vcf} {log}")
        shell("mv --verbose {prefix}.vcf.gz.tbi {snakemake.output.vcf}.tbi {log}")

    if snakemake.output.get("cnv"):
        shell("mv --verbose {prefix}.cnv.png {snakemake.output.cnv} {log}")

    if snakemake.output.get("hist"):
        shell("mv --verbose {prefix}.cov.pdf {snakemake.output.hist} {log}")

    if snakemake.output.get("spider"):
        shell("mv --verbose {prefix}.spider.pdf {snakemake.output.spider} {log}")
