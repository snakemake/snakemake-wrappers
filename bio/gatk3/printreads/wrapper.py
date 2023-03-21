__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com.com"
__license__ = "MIT"

import os

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
java_opts = get_java_opts(snakemake)


bqsr = snakemake.input.get("recal_data", "")
if bqsr:
    bqsr = f"--BQSR {bqsr}"


shell(
    "gatk3 {java_opts}"
    " --analysis_type PrintReads"
    " --input_file {snakemake.input.bam}"
    " --reference_sequence {snakemake.input.ref}"
    " {bqsr}"
    " {extra}"
    " --out {snakemake.output.bam}"
    " {log}"
)
