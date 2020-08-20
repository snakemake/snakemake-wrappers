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
    f" {extra}"
    f" -a {snakemake.input.left}"
    f" -b {snakemake.input.right}"
    f" > {snakemake.output})"
    f" {log}"
)
