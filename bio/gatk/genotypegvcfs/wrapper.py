__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
interval_file = snakemake.input.get("interval_file", "")
if interval_file:
    interval_file = "-L {}".format(interval_file)
dbsnp = snakemake.input.get("known", "")
if dbsnp:
    dbsnp = "-D {}".format(dbsnp)

# Allow for either an input gvcf or GenomicsDB
gvcf = snakemake.input.get("gvcf", "")
genomicsdb = snakemake.input.get("genomicsdb", "")
if gvcf:
    if genomicsdb:
        raise Exception("Only input.gvcf or input.genomicsdb expected, got both.")
    input_string = gvcf
else:
    if genomicsdb:
        input_string = "gendb://{}".format(genomicsdb)
    else:
        raise Exception("Expected input.gvcf or input.genomicsdb.")
tmp_dir = snakemake.params.get("tmp_dir", "")
if tmp_dir:
    tmp_dir = "--tmp-dir={}".format(tmp_dir)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "gatk --java-options '{java_opts}' GenotypeGVCFs {extra} "
    "-V {input_string} "
    "-R {snakemake.input.ref} "
    "{dbsnp} "
    "{interval_file} "
    "{tmp_dir} "
    "-O {snakemake.output.vcf} {log}"
)
