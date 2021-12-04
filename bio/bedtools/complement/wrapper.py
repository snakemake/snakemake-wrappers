__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "(bedtools complement"
    " {extra}"
    " -i {snakemake.input.in_file}"
    " -g {snakemake.input.genome}"
    " > {snakemake.output[0]})"
    " {log}"
)
