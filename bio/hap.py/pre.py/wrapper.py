__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"

import os
from os import path

## Extract arguments
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    "(pre.py"
    " --threads %s"
    " -r %s"
    " %s"
    " %s"
    " %s)"
    " %s"
    % (
        snakemake.threads,
        snakemake.params.genome,
        extra,
        snakemake.input.variants,
        snakemake.output,
        log,
    )
)
