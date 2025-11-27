__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

compress = "| bgzip" if snakemake.output[0].endswith(".gz") else ""

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "(bedtools complement"
    " {extra}"
    " -i {snakemake.input.in_file}"
    " -g {snakemake.input.genome}"
    " {compress}"
    " > {snakemake.output[0]})"
    " {log}"
)
