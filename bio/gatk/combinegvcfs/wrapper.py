__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os

from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
java_opts = snakemake.params.get("java_opts", "")
if "mem_mb" in snakemake.resources.keys() and not "-Xmx" in java_opts:
    java_opts += " -Xmx{}M".format(snakemake.resources["mem_mb"])

gvcfs = list(map("-V {}".format, snakemake.input.gvcfs))

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell(
    "gatk --java-options '{java_opts}' CombineGVCFs {extra} "
    "{gvcfs} "
    "-R {snakemake.input.ref} "
    "-O {snakemake.output.gvcf} {log}"
)
