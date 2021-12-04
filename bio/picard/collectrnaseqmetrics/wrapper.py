__author__ = "Brett Copeland"
__copyright__ = "Copyright 2021, Brett Copeland"
__email__ = "brcopeland@ucsd.edu"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

strand = snakemake.params.get("strand", "NONE")
extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "picard CollectRnaSeqMetrics "
    "{java_opts} {extra} "
    "INPUT={snakemake.input.bam} "
    "OUTPUT={snakemake.output} "
    "REF_FLAT={snakemake.input.refflat} "
    "STRAND_SPECIFICITY={strand} "
    "{log}"
)
