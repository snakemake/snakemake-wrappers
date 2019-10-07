__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"

import os
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "pindel -T {snakemake.threads} {snakemake.params.extra} -i {snakemake.input.config} "
    "-f {snakemake.input.ref} -o {snakemake.params.prefix} {log}"
)
