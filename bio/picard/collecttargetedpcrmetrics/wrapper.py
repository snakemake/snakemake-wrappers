__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@mail.com"
__license__ = "MIT"


import os


log = snakemake.log_fmt_shell()

extra = snakemake.params.get("extra", "")

os.system(
    f"picard CollectTargetedPcrMetrics "
    "{extra} "
    "INPUT={snakemake.input.bam} "
    "OUTPUT={snakemake.output[0]} "
    "AMPLICON_INTERVALS={snakemake.input.amplicon_intervals} "
    "TARGET_INTERVALS={snakemake.input.target_intervals} "
    "{log}"
)
