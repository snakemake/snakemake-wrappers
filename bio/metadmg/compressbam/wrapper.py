__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"


import tempfile
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


ref = snakemake.input.get("ref", "")
if ref:
    ref = f"--ref {ref}"


out_fmt = Path(snakemake.input.aln).suffix


shell("compressbam --threads {snakemake.threads} -hts {snakemake.input.aln} {ref} {extra} -type {out_fmt} -out {snakemake.output[0]} {log}")
