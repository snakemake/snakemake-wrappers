"""Snakemake wrapper for STAR index"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from snakemake.utils import makedirs

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

sjdb_overhang = snakemake.params.get("sjdbOverhang", "")
if sjdb_overhang:
    sjdb_overhang = f"--sjdbOverhang {sjdb_overhang}"

gtf = snakemake.input.get("gtf", "")
if gtf:
    gtf = f"--sjdbGTFfile {gtf}"


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "STAR"
        " --runThreadN {snakemake.threads}"  # Number of threads
        " --runMode genomeGenerate"  # Indexation mode
        " --genomeFastaFiles {snakemake.input.fasta}"  # Path to fasta files
        " {sjdb_overhang}"  # Read-len - 1
        " {gtf}"  # Highly recommended GTF
        " {extra}"  # Optional parameters
        " --outTmpDir {tmpdir}/STARtmp"  # Temp dir
        " --genomeDir {snakemake.output}"  # Path to output
        " {log}"  # Logging
    )
