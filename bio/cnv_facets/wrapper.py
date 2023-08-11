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
    input_data = f"-t {snakemake.input.tumor} -n {snakemake.input.normal}"
elif "pileup" in snakemake.input.keys():
    input_data = f"-p {snakemake.input.pileup}"
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
    shell("mv --verbose {prefix}.vcf.gz {output.vcf} {log}")
    shell("mv --verbose {prefix}.cnv.png {output.cnv} {log}")
    shell("mv --verbose {prefix}.cov.pdf {output.hist} {log}")
    shell("mv --verbose {prefix}.spider.pdf {output.spider} {log}")
    shell("mv --verbose {prefix}.csv.gz {output.pileup} {log}")