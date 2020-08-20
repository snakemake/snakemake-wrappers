__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com.com"
__license__ = "MIT"

import os

extra = snakemake.params.get("extra", "")
java_opts = snakemake.params.get("java_opts", "")

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

os.system(
    f"gatk3 {java_opts} -T IndelRealigner"
    f" {extra}"
    f" -I {input_bam}"
    f" -R {input_ref}"
    f" {input_known_string}"
    f" {bed}"
    f" --targetIntervals {input_target_intervals}"
    f" -o {snakemake.output}"
    f" {log}"
)
