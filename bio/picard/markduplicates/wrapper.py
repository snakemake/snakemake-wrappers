__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell()

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

bams = snakemake.input
if isinstance(bams, str):
    bams = [bams]
bams = list(map("--INPUT {}".format, bams))

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "picard MarkDuplicates"  # Tool and its subcommand
        " {java_opts}"  # Automatic java option
        " {extra}"  # User defined parmeters
        " {bams}"  # Input bam(s)
        " --TMP_DIR {tmpdir}"
        " --OUTPUT {snakemake.output.bam}"  # Output bam
        " --METRICS_FILE {snakemake.output.metrics}"  # Output metrics
        " {log}"  # Logging
    )
