__author__ = "Johannes Köster, Derek Croote"
__copyright__ = "Copyright 2020, Johannes Köster"
__email__ = "johannes.koester@uni-due.de"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell


def get_mem(snakemake, out_unit="MB"):
    # Store resources.mem in MB
    mem_mb = snakemake.resources.get("mem_gb", 0) * 1024
    if not mem_mb:
        mem_mb = snakemake.resources.get("mem_mb", 0)

    if out_unit == "MB":
        return mem_mb
    elif out_unit == "GB":
        return mem_mb / 1024
    else:
        raise valueError("invalid out_unit, only MB and GB supported.")


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


# Parse memory
mem = ""
mem_mb = get_mem(snakemake, "MB")


# Outdir
outdir = os.path.dirname(snakemake.output[0])
if outdir:
    outdir = f"--outdir {outdir}"


# Output compression
compress = ""
if mem_mb:
    mem = f"-m{mem_mb}"

for output in snakemake.output:
    out_name, out_ext = os.path.splitext(output)
    if out_ext == ".gz":
        compress += f"pigz -p {snakemake.threads} {out_name}; "
    elif out_ext == ".bz2":
        compress += f"pbzip2 -p{snakemake.threads} {mem} {out_name}; "


if mem_mb:
    mem = f"--mem {mem_mb}M"

with tempfile.TemporaryDirectory() as tmp:
    shell(
        "(fasterq-dump --temp {tmp} --threads {snakemake.threads} {mem} "
        "{extra} {outdir} {snakemake.wildcards.accession}; "
        "{compress}"
        ") {log}"
    )
