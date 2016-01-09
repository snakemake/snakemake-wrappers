__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os
from snakemake.shell import shell


prefix = os.path.splitext(snakemake.output.bam)[0]

shell(
    "samtools sort -@ {snakemake.threads} -o {snakemake.output[0]} "
    "-T {prefix} {snakemake.input[0]}")
