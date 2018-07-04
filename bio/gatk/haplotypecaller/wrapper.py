__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os

from snakemake.shell import shell

known = snakemake.input.get("known", "")
if known:
    known = "--dbsnp " + known

extra = snakemake.params.get("extra", "")
bams = snakemake.input.bam
if isinstance(bams, str):
    bams = [bams]
bams = list(map("-I {}".format, bams))

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell("gatk HaplotypeCaller {extra} "
      "-R {snakemake.input.ref} {bams} "
      "-ERC GVCF "
      "-O {snakemake.output.gvcf} {known} {log}")
