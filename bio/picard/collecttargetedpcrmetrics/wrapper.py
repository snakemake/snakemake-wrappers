__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@mail.com"
__license__ = "MIT"


import os


log = snakemake.log_fmt_shell()

extra = snakemake.params.get("extra", "")

os.system(
    f"picard CollectTargetedPcrMetrics "
    f"{extra} "
    f"INPUT={snakemake.input.bam} "
    f"OUTPUT={snakemake.output[0]} "
    f"AMPLICON_INTERVALS={snakemake.input.amplicon_intervals} "
    f"TARGET_INTERVALS={snakemake.input.target_intervals} "
    f"{log}"
)
