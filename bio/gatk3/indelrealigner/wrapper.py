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
input_known = snakemake.input.known
input_ref = snakemake.input.ref
input_target_intervals = snakemake.input.target_intervals

bed = snakemake.params.get("bed", None)
if bed is not None:
    bed = "-L " + bed
else:
    bed = ""

input_known_string = ""
for known in input_known:
    input_known_string = input_known_string + " -known {}".format(known)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "gatk3 {java_opts} -T IndelRealigner"
    " {extra}"
    " -I {input_bam}"
    " -R {input_ref}"
    " {input_known_string}"
    " {bed}"
    " --targetIntervals {input_target_intervals}"
    " -o {snakemake.output}"
    " {log}"
)
