__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "vep_install --AUTO cf "
    "--SPECIES {snakemake.params.species} "
    "--ASSEMBLY {snakemake.params.build} "
    "--VERSION {snakemake.params.release} "
    "--CACHEDIR {snakemake.output} "
    "--CONVERT "
    "--NO_UPDATE "
    "{extra} {log}"
)
