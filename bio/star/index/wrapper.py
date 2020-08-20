"""Snakemake wrapper for STAR index"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")
sjdb_overhang = snakemake.params.get("sjdbOverhang", "100")

gtf = snakemake.input.get("gtf")
if gtf is not None:
    gtf = "--sjdbGTFfile " + gtf
    sjdb_overhang = "--sjdbOverhang " + sjdb_overhang
else:
    gtf = sjdb_overhang = ""

os.makedirs(snakemake.output)

command = (
    f"STAR "  # Tool
    f"--runMode genomeGenerate "  # Indexation mode
    f"{extra} "  # Optional parameters
    f"--runThreadN {snakemake.threads} "  # Number of threads
    f"--genomeDir {snakemake.output} "  # Path to output
    f"--genomeFastaFiles {snakemake.input.fasta} "  # Path to fasta files
    f"{sjdb_overhang} "  # Read-len - 1
    f"{gtf} "  # Highly recommended GTF
    f"{log}"  # Logging
)
print(command)
os.system(command)
