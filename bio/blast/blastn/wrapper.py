__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2021, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

format = snakemake.params.get("format", "")
blastdb = snakemake.input.get("blastdb", "")[0]
db_name = path.splitext(blastdb)[0]

if format:
    out_format = " -outfmt '{}'".format(format)

shell(
    "blastn"
    " -query {snakemake.input.query}"
    " {out_format}"
    " {snakemake.params.extra}"
    " -db {db_name}"
    " -num_threads {snakemake.threads}"
    " -out {snakemake.output[0]}"
)
