__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "picard MarkDuplicates {snakemake.params} INPUT={snakemake.input} "
    "OUTPUT={snakemake.output.bam} METRICS_FILE={snakemake.output.metrics} "
    "{log}"
)
