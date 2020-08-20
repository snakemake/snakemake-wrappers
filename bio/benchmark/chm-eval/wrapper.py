__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

kit = snakemake.input.kit
vcf = snakemake.input.vcf
build = snakemake.params.build
extra = snakemake.params.get("extra", "")

if not snakemake.output[0].endswith(".summary"):
    raise ValueError("Output file must end with .summary")
out = snakemake.output[0][:-8]

os.system(f"({kit}/run-eval -g {build} -o {out} {extra} {vcf} | sh) {log}")
