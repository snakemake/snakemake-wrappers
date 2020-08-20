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

os.systeml(
    f"STAR "  # Tool
    "--runMode genomeGenerate "  # Indexation mode
    "{extra} "  # Optional parameters
    "--runThreadN {snakemake.threads} "  # Number of threads
    "--genomeDir {snakemake.output} "  # Path to output
    "--genomeFastaFiles {snakemake.input.fasta} "  # Path to fasta files
    "{sjdb_overhang} "  # Read-len - 1
    "{gtf} "  # Highly recommended GTF
    "{log}"  # Logging
)
