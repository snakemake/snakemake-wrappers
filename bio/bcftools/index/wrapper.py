__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os

## Extract arguments
extra = snakemake.params.get("extra", "")

os.system(f"bcftools index {extra} {snakemake.input[0]}")
