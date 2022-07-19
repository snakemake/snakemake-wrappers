__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import os
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


ref = snakemake.input.get("ref", "")
if ref:
    ref = f"-r {ref}"

gff = snakemake.input.get("gff", "")
if gff:
    gff = f"--features {gff}"

pacbio = snakemake.input.get("pacbio", "")
if pacbio:
    pacbio = f"--pacbio {pacbio}"

output_dir = os.path.commonpath(snakemake.output)


shell(
    "quast --threads {snakemake.threads} {ref} {gff} {pacbio} {extra} -o {output_dir} {snakemake.input.fasta} {log}"
)
