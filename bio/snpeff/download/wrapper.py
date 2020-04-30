__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell
from os import path
import shutil
import tempfile

reference = snakemake.params.reference
outdir = path.dirname(snakemake.output[0])
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell("snpEff download -dataDir {outdir} {reference} {log}")
