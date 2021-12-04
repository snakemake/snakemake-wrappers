__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell()

extra = snakemake.params
java_opts = get_java_opts(snakemake)


shell(
    "picard CollectInsertSizeMetrics {java_opts} {extra} "
    "INPUT={snakemake.input} OUTPUT={snakemake.output.txt} "
    "HISTOGRAM_FILE={snakemake.output.pdf} {log}"
)
