__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
java_opts = snakemake.params.get("java_opts", "")

shell(
    "gatk --java-options '{java_opts}' BaseRecalibrator {extra} "
    "-R {snakemake.input.ref} -I {snakemake.input.bam} "
    "-O {snakemake.output.recal_table} {known} {log}"
)
