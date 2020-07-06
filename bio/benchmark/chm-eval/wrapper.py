__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell

kit = snakemake.input.kit
vcf = snakemake.input.vcf
build = snakemake.params.build

shell("{kit}/run-eval -g {build} {extra} {vcf} | sh")
