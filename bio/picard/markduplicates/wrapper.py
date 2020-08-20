__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

os.system(
    f"picard MarkDuplicates {snakemake.params} INPUT={snakemake.input} "
    "OUTPUT={snakemake.output.bam} METRICS_FILE={snakemake.output.metrics} "
    "{log}"
)
