__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "picard CollectGcBiasMetrics "
    "{java_opts} {extra} "
    "INPUT={snakemake.input.bam} "
    "OUTPUT={snakemake.output.metrics} "
    "CHART={snakemake.output.chart} "
    "SUMMARY_OUTPUT={snakemake.output.summary} "
    "REFERENCE_SEQUENCE={snakemake.input.ref} "
    "{log}"
)
