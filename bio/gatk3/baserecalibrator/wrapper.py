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


bed = snakemake.params.get("bed", "")
if bed:
    bed = f"--intervals {bed}"


input_known = snakemake.input.get("known", "")
if input_known:
    if isinstance(input_known, str):
        input_known = [input_known]
    input_known = list(map("--knownSites {}".format, input_known))


shell(
    "gatk3 {java_opts}"
    " --analysis_type BaseRecalibrator"
    " --num_cpu_threads_per_data_thread {snakemake.threads}"
    " --input_file {snakemake.input.bam}"
    " {input_known}"
    " --reference_sequence {snakemake.input.ref}"
    " {bed}"
    " {extra}"
    " --out {snakemake.output}"
    " {log}"
)
