__author__ = "Jan Forster"
__copyright__ = "Copyright 2021, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import os
from snakemake.shell import shell

shell(
    "sambamba index {snakemake.params.extra} -t {snakemake.threads} "
    "{snakemake.input[0]} {snakemake.output[0]}"
)
