__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os
from pathlib import Path

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

os.system(
    f"vep_install --AUTO cf "
    f"--SPECIES {snakemake.params.species} "
    f"--ASSEMBLY {snakemake.params.build} "
    f"--CACHE_VERSION {snakemake.params.release} "
    f"--CACHEDIR {snakemake.output} "
    f"--CONVERT "
    f"--NO_UPDATE {log}"
)
