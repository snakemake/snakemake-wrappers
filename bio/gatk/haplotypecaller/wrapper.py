__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

known = snakemake.input.get("known", "")
if known:
    known = "--dbsnp " + str(known)

bam_output = snakemake.output.get("bam", "")
if bam_output:
    bam_output = "--bam-output " + str(bam_output)

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

bams = snakemake.input.bam
if isinstance(bams, str):
    bams = [bams]
bams = list(map("-I {}".format, bams))

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "gatk --java-options '{java_opts}' HaplotypeCaller {extra} "
    "-R {snakemake.input.ref} {bams} "
    "-ERC GVCF {bam_output} "
    "-O {snakemake.output.gvcf} {known} {log}"
)
