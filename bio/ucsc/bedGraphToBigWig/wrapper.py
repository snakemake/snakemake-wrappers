"""Snakemake wrapper for *.bedGraph to *.bw conversion using UCSC bedGraphToBigWig tool."""
# http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/FOOTER.txt

__author__ = "Roman Chernyatchik"
__copyright__ = "Copyright (c) 2019 JetBrains"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

os.system(
    f"bedGraphToBigWig {extra}"
    f" {snakemake.input.bedGraph} {snakemake.input.chromsizes}"
    f" {snakemake.output} {log}"
)
