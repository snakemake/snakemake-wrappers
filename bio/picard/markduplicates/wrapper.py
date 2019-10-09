__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

java_opt = snakemake.params.get("java_options", "")
extra = snakemake.params.get("extra", "")

shell("picard {java_options} MarkDuplicates {extra} INPUT={snakemake.input} "
      "OUTPUT={snakemake.output.bam} METRICS_FILE={snakemake.output.metrics} "
      "&> {snakemake.log}")
