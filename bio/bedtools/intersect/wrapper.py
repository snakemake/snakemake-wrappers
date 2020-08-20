__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"

import os

## Extract arguments
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

os.system(
    f"(bedtools intersect"
    " {extra}"
    " -a {snakemake.input.left}"
    " -b {snakemake.input.right}"
    " > {snakemake.output})"
    " {log}"
)
