__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

plugins = ",".join(snakemake.params.plugins)

shell(
    "vep_install --AUTO p "
    "--PLUGINS {plugins} "
    "--PLUGINSDIR {snakemake.output} "
    "{log}"
)
