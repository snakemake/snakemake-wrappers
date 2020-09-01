__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
url = (
    "https://github.com/lh3/CHM-eval/releases/"
    "download/{tag}/CHM-evalkit-{version}.tar"
).format(version=snakemake.params.version, tag=snakemake.params.tag)

os.makedirs(snakemake.output[0])
shell(
    "(curl -L {url} | tar --strip-components 1 -C {snakemake.output[0]} -xf - &&"
    "(cd {snakemake.output[0]}; chmod +x htsbox run-eval k8)) {log}"
)
