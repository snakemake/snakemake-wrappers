"""Snakemake wrapper for GATK VariantsToTable"""

__author__ = "Dmitry Bespiatykh"
__copyright__ = "Copyright 2023, Dmitry Bespiatykh"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


intervals = snakemake.input.get("intervals", "")
if not intervals:
    intervals = snakemake.params.get("intervals", "")
if intervals:
    intervals = "--intervals {}".format(intervals)


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' VariantsToTable"
        " --variant {snakemake.input.vcf}"
        " {intervals}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output.tab}"
        " {log}"
    )
