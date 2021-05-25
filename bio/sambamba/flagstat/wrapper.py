__author__ = "Jan Forster"
__copyright__ = "Copyright 2021, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"


import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "sambamba flagstat {snakemake.params.extra} -t {snakemake.threads} "
    "{snakemake.input[0]} > {snakemake.output[0]} "
    "{log}"
)
