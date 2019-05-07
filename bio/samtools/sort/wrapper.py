__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os
from snakemake.shell import shell


prefix = os.path.splitext(snakemake.output[0])[0]
threads = (
    "" if snakemake.threads <= 1
    else " -@ {} ".format(snakemake.threads - 1)
)

shell(
    "samtools sort {snakemake.params} {threads} -o {snakemake.output[0]} "
    "-T {prefix} {snakemake.input[0]}")
