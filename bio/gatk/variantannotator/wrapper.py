__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


input = snakemake.input.get("aln", "")
if input:
    input = f"--input {input}"

reference = snakemake.input.get("ref", "")
if reference:
    reference = f"--reference {reference}"

dbsnp = snakemake.input.get("known", "")
if dbsnp:
    dbsnp = f"--dbsnp {dbsnp}"

intervals = snakemake.input.get("intervals", "")
if not intervals:
    intervals = snakemake.params.get("intervals", "")
if intervals:
    intervals = "--intervals {}".format(intervals)

resources = [
    f"--resource:{name} {file}"
    for name, file in snakemake.input.items()
    if name not in ["vcf", "aln", "ref", "known", "intervals", "bai"]
]


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' VariantAnnotator"
        " --variant {snakemake.input.vcf}"
        " {input}"
        " {reference}"
        " {dbsnp}"
        " {intervals}"
        " {resources}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output.vcf}"
        " {log}"
    )
