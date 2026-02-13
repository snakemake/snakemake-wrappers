__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2020, Christopher Schröder"
__email__ = "christopher.schroeder@tu-dortmund.de"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

# Extract arguments
extra = snakemake.params.get("extra", "")
embed_ref = snakemake.params.get("embed_ref", False)
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

if snakemake.output.bam.endswith(".cram"):
    embed = " --output-fmt-option embed_ref" if embed_ref else ""
    output = "/dev/stdout"
    pipe_cmd = (
        "| samtools view --with-header --reference {snakemake.input.ref} --output-fmt cram {embed} --output {snakemake.output.bam}"
    )
else:
    output = snakemake.output.bam
    pipe_cmd = ""

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(gatk --java-options '{java_opts}' ApplyBQSR"
        " --input {snakemake.input.bam}"
        " --bqsr-recal-file {snakemake.input.recal_table}"
        " --reference {snakemake.input.ref}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {output}" + pipe_cmd + ") {log}"
    )
