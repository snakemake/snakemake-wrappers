__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"

import os
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("pindel2vcf {snakemake.params.extra} -p {snakemake.input.pindel} -f {snakemake.input.ref} -R {snakemake.params.refname} -d {snakemake.params.refdate} -v {snakemake.output[0]} {log}")
