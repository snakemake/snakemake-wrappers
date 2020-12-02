__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com.com"
__license__ = "MIT"

import os

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

input_bam = snakemake.input.bam
input_recal_data = snakemake.input.recal_data
input_ref = snakemake.input.ref

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "gatk3 {java_opts} -T PrintReads"
    " {extra}"
    " -I {input_bam}"
    " -R {input_ref}"
    " -BQSR {input_recal_data}"
    " -o {snakemake.output}"
    " {log}"
)
