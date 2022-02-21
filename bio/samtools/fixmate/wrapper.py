"""Snakemake wrapper for samtools fixmate"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake.utils import makedirs
from snakemake_wrapper_utils.samtools import get_samtools_opts

samtools_opts = get_samtools_opts(
    snakemake, parse_write_index=False, parse_output=False
)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "samtools fixmate {samtools_opts} {extra} {snakemake.input[0]} {snakemake.output[0]} {log}"
)
