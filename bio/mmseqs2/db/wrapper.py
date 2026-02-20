__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


input = snakemake.input
if isinstance(input, list):
    input = os.path.commonprefix(input)

# TODO: arbitrary output file names
out = snakemake.output
if isinstance(out, list):
    out = os.path.commonprefix(out).rstrip("_")


with tempfile.TemporaryDirectory() as tmpdir:
    # Modules with threads
    if snakemake.params.module in ["databases"]:
        extra = f"--threads {snakemake.threads} {extra}"
    # Modules with no temp folder
    if snakemake.params.module in ["createdb"]:
        tmpdir = ""

    shell("mmseqs {snakemake.params.module} {input} {out} {tmpdir} {extra} {log}")
