"""Snakemake wrapper for *.bedGraph to *.bw conversion using UCSC bedGraphToBigWig tool."""

# http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/FOOTER.txt

__author__ = "Roman Chernyatchik"
__copyright__ = "Copyright (c) 2019 JetBrains"
__email__ = "roman.chernyatchik@jetbrains.com"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

shell(
    "bedGraphToBigWig {extra}"
    " {snakemake.input.bedGraph} {snakemake.input.chromsizes}"
    " {snakemake.output} {log}"
)
