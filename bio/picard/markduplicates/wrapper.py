__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
bams = snakemake.input
if isinstance(bams, str):
    bams = [bams]
bams = list(map("INPUT={}".format, bams))

shell(
    "picard MarkDuplicates "  # Tool and its subcommand
    "{java_opts} "  # Automatic java option
    "{extra} "  # User defined parmeters
    "{bams} "  # Input bam(s)
    "OUTPUT={snakemake.output.bam} "  # Output bam
    "METRICS_FILE={snakemake.output.metrics} "  # Output metrics
    "{log}"  # Logging
)
