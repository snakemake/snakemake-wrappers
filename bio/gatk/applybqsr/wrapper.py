__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2020, Christopher Schröder"
__email__ = "christopher.schroeder@tu-dortmund.de"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

# Extract arguments
extra = snakemake.params.get("extra", "")
reference = snakemake.input.get("ref")
embed_ref = snakemake.params.get("embed_ref", False)
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

if snakemake.output.bam.endswith(".cram") and embed_ref:
    output = "/dev/stdout"
    pipe_cmd = " | samtools view -h -O cram,embed_ref -T {reference} -o {snakemake.output.bam} -"
else:
    output = snakemake.output.bam
    pipe_cmd = ""

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(gatk --java-options '{java_opts}' ApplyBQSR"
        " --input {snakemake.input.bam}"
        " --bqsr-recal-file {snakemake.input.recal_table}"
        " --reference {reference}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {output}" + pipe_cmd + ") {log}"
    )
