# coding: utf-8

"""Snakemake wrapper for crabz"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2026, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format, is_arg

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


def crabz_format(file_path):
    fmt = get_format(file_path, ignore_compression=False)
    print(fmt)
    if fmt == "bgzip":
        return "bgzf"
    return fmt


available_compression_formats = {"gzip", "bgzf", "mgzip", "zlib", "deflate", "snap"}

input_file_format = crabz_format(str(snakemake.input))
if input_file_format in available_compression_formats:
    extra += f" --decompress"
    if is_arg("format", extra):
        extra += f" --format '{input_file_format}'"
elif is_arg("format", extra):
    extra += f" --format '{crabz_format(str(snakemake.output))}'"

shell(
    "crabz --compression-threads {snakemake.threads} {extra} "
    "--output {snakemake.output:q} {snakemake.input} {log}"
)
