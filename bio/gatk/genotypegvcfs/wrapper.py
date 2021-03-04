__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

input_gvcf = snakemake.input.gvcf
if os.path.isdir(input_gvcf):
    input_gvcf = "gendb://" + input_gvcf


shell(
    "gatk --java-options '{java_opts}' GenotypeGVCFs {extra} "
    "-V {input_gvcf} "
    "-R {snakemake.input.ref} "
    "-O {snakemake.output.vcf} {log}"
)
