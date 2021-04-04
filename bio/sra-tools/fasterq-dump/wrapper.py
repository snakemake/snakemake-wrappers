__author__ = "Johannes Köster, Derek Croote"
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


compress = ""
for output in snakemake.output:
    out_name, out_ext = os.path.splitext(output[0])
    if out_ext == ".gz":
        compress += "gzip {}; ".format(out_name)
    elif out_ext == ".bz2":
        compress += "bzip2 {}; ".format(out_name)


with tempfile.TemporaryDirectory() as tmp:
    shell(
        "(fasterq-dump --temp {tmp} --threads {snakemake.threads} "
        "{extra} {outdir} {snakemake.wildcards.accession}; "
        "{compress}"
        ") {log}"
    )
