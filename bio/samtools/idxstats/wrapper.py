__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"


import os

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(f"samtools idxstats {snakemake.input.bam} > {snakemake.output[0]} {log}")
