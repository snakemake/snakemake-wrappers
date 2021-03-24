__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2021, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell
from os import path
from pathlib import Path

log = snakemake.log
out = snakemake.output[0]

db_type = ""
out_name = "{}/{}".format(path.dirname(out), Path(path.basename(out)).stem)
ext = Path(out).suffix

if ext.startswith(".n"):
    db_type = "nucl"
elif ext.startswith(".p"):
    db_type = "prot"

shell(
    "makeblastdb"
    " -in {snakemake.input.fasta}"
    " -dbtype {db_type}"
    " {snakemake.params}"
    " -logfile {log}"
    " -out {out_name}"
)
