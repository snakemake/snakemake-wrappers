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


bed = snakemake.input.get("bed", "")
if bed:
    bed = f"--intervals {bed}"


known = snakemake.input.get("known", "")
if known:
    if isinstance(known, str):
        known = f"--knownAlleles {known}"
    else:
        known = list(map("----knownAlleles {}".format, known))


output_bai = snakemake.output.get("bai", None)
if output_bai is None:
    extra += " --disable_bam_indexing"


shell(
    "gatk3 {java_opts}"
    " --analysis_type IndelRealigner"
    " --input_file {snakemake.input.bam}"
    " --reference_sequence {snakemake.input.ref}"
    " {known}"
    " {bed}"
    " --targetIntervals {snakemake.input.target_intervals}"
    " {extra}"
    " --out {snakemake.output.bam}"
    " {log}"
)
