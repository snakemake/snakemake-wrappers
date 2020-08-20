__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os


os.system(
    f"samtools index {snakemake.params} {snakemake.input[0]} {snakemake.output[0]}"
)
