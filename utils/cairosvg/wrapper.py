__author__ = "Johannes Köster"
__copyright__ = "Copyright 2017, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"

import os
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

_, ext = os.path.splitext(snakemake.output[0])

if ext not in (".png", ".pdf", ".ps", ".svg"):
    raise ValueError("invalid file extension: '{}'".format(ext))
fmt = ext[1:]

shell("cairosvg -f {fmt} {snakemake.input[0]} -o {snakemake.output[0]}")
