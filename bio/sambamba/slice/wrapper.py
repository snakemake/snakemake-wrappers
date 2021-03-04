__author__ = "Jan Forster"
__copyright__ = "Copyright 2021, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import os
from snakemake.shell import shell

shell(
    "sambamba slice "
    "{snakemake.input[0]} {snakemake.params.region} > {snakemake.output[0]}"
)
