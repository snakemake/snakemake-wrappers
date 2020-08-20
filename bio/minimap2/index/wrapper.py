__author__ = "Tom Poorten"
__copyright__ = "Copyright 2017, Tom Poorten"
__email__ = "tom.poorten@gmail.com"
__license__ = "MIT"

import os

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

os.system(
    f"(minimap2 -t {snakemake.threads} {extra} "
    "-d {snakemake.output[0]} {snakemake.input.target}) {log}"
)
