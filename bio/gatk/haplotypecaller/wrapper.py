__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os
import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

bams = snakemake.input.bam
if isinstance(bams, str):
    bams = [bams]
bams = list(map("--input {}".format, bams))

intervals = snakemake.input.get("intervals", "")
if not intervals:
    intervals = snakemake.params.get("intervals", "")
if intervals:
    intervals = "--intervals {}".format(intervals)

known = snakemake.input.get("known", "")
if known:
    known = "--dbsnp " + str(known)

bam_output = snakemake.output.get("bam", "")
if bam_output:
    bam_output = "--bam-output " + str(bam_output)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' HaplotypeCaller"
        " --native-pair-hmm-threads {snakemake.threads}"
        " {bams}"
        " --reference {snakemake.input.ref}"
        " {intervals}"
        " {known}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --emit-ref-confidence GVCF {bam_output}"
        " --output {snakemake.output.gvcf}"
        " {log}"
    )
