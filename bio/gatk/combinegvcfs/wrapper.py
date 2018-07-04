__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os

from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
gvcfs = list(map("-V {}".format, snakemake.input.gvcfs))

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
shell("gatk CombineGVCFs {extra} "
      "{gvcfs} "
      "-R {snakemake.input.ref} "
      "-O {snakemake.output.gvcf} {log}")
