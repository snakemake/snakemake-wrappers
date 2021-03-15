"""Snakemake wrapper for samtools fixmate"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import os.path as op

from snakemake.shell import shell
from snakemake.utils import makedirs

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")

# Samtools' threads parameter lists ADDITIONAL threads.
# that is why threads - 1 has to be given to the -@ parameter
threads = "" if snakemake.threads <= 1 else " -@ {} ".format(snakemake.threads - 1)

makedirs(op.dirname(snakemake.output[0]))

shell(
    "samtools fixmate {extra} {threads}"
    " {snakemake.input[0]} {snakemake.output[0]} {log}"
)
