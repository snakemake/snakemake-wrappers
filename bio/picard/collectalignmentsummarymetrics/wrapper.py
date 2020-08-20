__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os


log = snakemake.log_fmt_shell()


os.system(
    f"picard CollectAlignmentSummaryMetrics {snakemake.params} "
    f"INPUT={snakemake.input.bam} OUTPUT={snakemake.output[0]} "
    f"REFERENCE_SEQUENCE={snakemake.input.ref} {log}"
)
