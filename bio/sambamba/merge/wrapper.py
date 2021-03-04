__author__ = "Jan Forster"
__copyright__ = "Copyright 2021, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "sambamba merge {snakemake.params.extra} -t {snakemake.threads} "
    "{snakemake.output[0]} {snakemake.input} "
    "{log}"
)
