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
output_bam = snakemake.output.bam

# Getting memory in megabytes, if java opts is not filled with -Xmx parameter
# By doing so, backward compatibility is preserved
if "mem_mb" in snakemake.resources.keys() and not "-Xmx" in java_opts:
    java_opts += " -Xmx{}M".format(snakemake.resources["mem_mb"])

# Getting memory in gigabytes, for user convenience. Please prefer the use
# of mem_mb over mem_gb as advised in documentation.
elif "mem_gb" in snakemake.resources.keys() and not "-Xmx" in java_opts:
    java_opts += " -Xmx{}G".format(snakemake.resources["mem_gb"])

# Getting java temp directory from output files list, if -Djava.io.tmpdir
# is not provided in java parameters. By doing so, backward compatibility is
# not broken.
if "java_temp" in snakemake.output.keys() and not "-Djava.io.tmpdir" in java_opts:
    java_opts += " -Djava.io.tmpdir={}".format(snakemake.output["java_temp"])

bed = snakemake.params.get("bed", None)
if bed is not None:
    bed = "-L " + bed
else:
    bed = ""

input_known_string = ""
for known in input_known:
    input_known_string = input_known_string + " -known {}".format(known)

output_bai = snakemake.output.get("bai", None)
if output_bai is None:
    extra += "--disable_bam_indexing"

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "gatk3 {java_opts} -T IndelRealigner"
    " {extra}"
    " -I {input_bam}"
    " -R {input_ref}"
    " {input_known_string}"
    " {bed}"
    " --targetIntervals {input_target_intervals}"
    " -o {output_bam}"
    " {log}"
)
