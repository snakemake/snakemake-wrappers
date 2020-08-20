__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


import os


log = snakemake.log_fmt_shell()


os.system(
    f"picard CollectInsertSizeMetrics {snakemake.params} "
    "INPUT={snakemake.input} OUTPUT={snakemake.output.txt} "
    "HISTOGRAM_FILE={snakemake.output.pdf} {log}"
)
