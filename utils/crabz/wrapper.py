# coding: utf-8

"""Snakemake wrapper for crabz"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2026, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

def guess_compression_format(path: str) -> str:
    """Try to guess compression format among the formats available in crabz"""
    if path.endswith(".gz"):
        return " --format gzip"
    elif path.endswith((".bgz", ".bz")):
        return " --format bgzf"
    elif path.endswith(".mgz"):
        return " --format mgzip"
    elif path.endswith((".zz", ".Z")):
        return " --format zlib"
    elif path.endswith((".snappy", ".snap")):
        return " --format snap"
    return ""


compression_formats = (".gz", ".bgz", "mgz", "zz", "deflat", "snappy", "sz")
infile = str(snakemake.input)
if infile.endswith(compression_formats):
    extra += " --decompress"
    if "--format" not in extra:
        extra += guess_compression_format(infile)
elif "--format" not in extra:
    extra += guess_compression_format(str(snakemake.output))


shell(
    "crabz --compression-threads {snakemake.threads} {extra} "
    "--output {snakemake.output:q} {snakemake.input} {log}"
)
