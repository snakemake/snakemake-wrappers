__author__ = "Jan Forster"
__copyright__ = "Copyright 2020, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"

from snakemake.shell import shell
import os.path as path
import sys

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


class PrefixNotSupportedError(Exception):
    pass


if "-prefix" in extra:
    raise PrefixNotSupportedError(
        "The use of the -prefix parameter is not yet supported in this wrapper"
    )

shell("(mergePeaks" " {snakemake.input}" " {extra}" " > {snakemake.output})" " {log}")
