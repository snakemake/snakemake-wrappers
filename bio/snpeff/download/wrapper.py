__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell
from pathlib import Path

reference = snakemake.params.reference
outdir = Path(snakemake.output[0]).parent.resolve()
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

if "mem_mb" in snakemake.resources.keys():
    extra += " -Xmx{}M".format(snakemake.resources["mem_mb"])

shell("snpEff download -dataDir {outdir} {reference} {log}")
