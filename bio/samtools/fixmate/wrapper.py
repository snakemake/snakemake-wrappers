"""Snakemake wrapper for samtools fixmate"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake.utils import makedirs

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")
# Samtools' threads parameter lists ADDITIONAL threads.
threads = (
    "" if snakemake.threads <= 1
    else " -@ {} ".format(snakemake.threads - 1)
)

shell("samtools fixmate {extra} {threads}"
      " {snakemake.input[0]} {snakemake.output[0]}")
