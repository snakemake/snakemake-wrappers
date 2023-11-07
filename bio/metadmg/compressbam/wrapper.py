__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from pathlib import Path
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


ref = snakemake.input.get("ref", "")
if ref:
    ref = f"--ref {ref}"


shell(
    "compressbam --threads {snakemake.threads} --input {snakemake.input.aln} {ref} {extra} --output {snakemake.output[0]} {log}"
)
