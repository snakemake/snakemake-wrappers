__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2021, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell
from os import path
from pathlib import Path

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

out = snakemake.output[0]
out_name = "{}/{}".format(path.dirname(out), Path(path.basename(out)).stem)

shell(
    "(makeblastdb"
    " -in {snakemake.input.fasta}"
    " -dbtype {snakemake.params.db_type}"
    " {snakemake.params.extra}"
    " -out {out_name}) {log}"
)
