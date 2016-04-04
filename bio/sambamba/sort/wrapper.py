__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import os
from snakemake.shell import shell

shell(
    "sambamba sort {snakemake.params} -t {snakemake.threads} "
    "-o {snakemake.output[0]} {snakemake.input[0]}")
