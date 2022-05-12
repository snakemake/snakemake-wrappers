__author__ = "Johannes Köster, Christopher Schröder"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell()

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

bams = snakemake.input.bams
if isinstance(bams, str):
    bams = [bams]
bams = list(map("--INPUT {}".format, bams))

if snakemake.output.bam.endswith(".cram"):
    output = "/dev/stdout"
    if snakemake.params.embed_ref:
        view_options = "-O cram,embed_ref"
    else:
        view_options = "-O cram"
    convert = f" | samtools view -@ {snakemake.threads} {view_options} --reference {snakemake.input.ref} -o {snakemake.output.bam}"
else:
    output = snakemake.output.bam
    convert = ""

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(picard MarkDuplicates"  # Tool and its subcommand
        " {java_opts}"  # Automatic java option
        " {extra}"  # User defined parmeters
        " {bams}"  # Input bam(s)
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {output}"  # Output bam
        " --METRICS_FILE {snakemake.output.metrics}"  # Output metrics
        " {convert} ) {log}"  # Logging
    )
