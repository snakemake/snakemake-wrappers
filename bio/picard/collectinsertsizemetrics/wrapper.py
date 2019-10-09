__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


from snakemake.shell import shell


log = snakemake.log_fmt_shell()
extra = snakemake.params.get("extra", "")
java_options = snakemake.params.get("java_options", "")

shell("picard {java_options} CollectInsertSizeMetrics {extra} "
      "INPUT={snakemake.input} OUTPUT={snakemake.output.txt} "
      "HISTOGRAM_FILE={snakemake.output.pdf} {log}")
