__author__ = "Johannes Köster, Christopher Schröder"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts
from snakemake_wrapper_utils.samtools import get_samtools_opts, infer_out_format


log = snakemake.log_fmt_shell()
extra = snakemake.params.get("extra", "")
# the --SORTING_COLLECTION_SIZE_RATIO default of 0.25 might
# indicate a JVM memory overhead of that proportion
java_opts = get_java_opts(snakemake, java_mem_overhead_factor=0.3)
samtools_opts = get_samtools_opts(snakemake)


tool = "MarkDuplicates"
if snakemake.params.get("withmatecigar", False):
    tool = "MarkDuplicatesWithMateCigar"


bams = snakemake.input.bams
if isinstance(bams, str):
    bams = [bams]
bams = list(map("--INPUT {}".format, bams))


output = snakemake.output.bam
output_fmt = infer_out_format(output)
convert = ""
if output_fmt == "CRAM":
    output = "/dev/stdout"

    # NOTE: output format inference should be done by snakemake-wrapper-utils. Keeping it here for backwards compatibility.
    if snakemake.params.get("embed_ref", False):
        samtools_opts += ",embed_ref"

    convert = f" | samtools view {samtools_opts}"
elif output_fmt == "BAM" and snakemake.output.get("idx"):
    extra += " --CREATE_INDEX"


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(picard {tool}"  # Tool and its subcommand
        " {java_opts}"  # Automatic java option
        " {extra}"  # User defined parmeters
        " {bams}"  # Input bam(s)
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {output}"  # Output bam
        " --METRICS_FILE {snakemake.output.metrics}"  # Output metrics
        " {convert}) {log}"  # Logging
    )


output_prefix = Path(snakemake.output.bam).with_suffix("")
if snakemake.output.get("idx"):
    if output_fmt == "BAM" and snakemake.output.idx != str(output_prefix) + ".bai":
        shell("mv {output_prefix}.bai {snakemake.output.idx}")
