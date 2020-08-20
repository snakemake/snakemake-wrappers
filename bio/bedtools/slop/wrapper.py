__author__ = "Jan Forster"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de"
__license__ = "MIT"

import os

## Extract arguments
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

os.system(
    f"(bedtools slop"
    f" {extra}"
    f" -i {snakemake.input[0]}"
    f" -g {snakemake.params.genome}"
    f" > {snakemake.output})"
    f" {log}"
)
