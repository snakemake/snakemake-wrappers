__author__ = "Johannes Köster"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

outdir = os.path.dirname(snakemake.output[0])
if outdir:
    outdir = "--outdir {}".format(outdir)

extra = snakemake.params.get("extra", "")

with tempfile.TemporaryDirectory() as tmp:
    shell(
        "fasterq-dump --temp {tmp} {extra} {outdir} {snakemake.wildcards.accession} {log}"
    )
