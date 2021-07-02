__author__ = "Johannes Köster, Derek Croote"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


outdir = os.path.dirname(snakemake.output[0])
if outdir:
    outdir = f"--outdir {outdir}"


compress = ""
for output in snakemake.output:
    out_name, out_ext = os.path.splitext(output)
    if out_ext == ".gz":
        compress += f"pigz -p {snakemake.threads} {out_name}; "
    elif out_ext == ".bz2":
        compress += f"pbzip2 -p{snakemake.threads} {out_name}; "


with tempfile.TemporaryDirectory() as tmp:
    shell(
        "(fasterq-dump --temp {tmp} --threads {snakemake.threads} "
        "{extra} {outdir} {snakemake.wildcards.accession}; "
        "{compress}"
        ") {log}"
    )
