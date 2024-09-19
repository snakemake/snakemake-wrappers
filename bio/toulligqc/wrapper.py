__author__ = "Salomé Brunon"
__copyright__ = "Copyright 2024, Salomé Brunon"
__email__ = "salome.brunon@gmail.com"
__license__ = "CECILL-2.1"

from snakemake.shell import shell
from pathlib import Path

if snakemake.input[0].endswith(".gz"):
    input_path = Path(snakemake.input[0].removesuffix(".gz"))
else:
    input_path = Path(snakemake.input[0])

if input_path.suffix in [".fastq", ".fq"]:
    input_flag = "--fastq "
elif input_path.suffix == ".bam":
    input_flag = "--bam "
else:
    input_flag = "--sequencing-summary-source "

outdir = Path(snakemake.output[0]).parent

shell("toulligqc {extra} {input_flag} {snakemake.input} -n {outdir} {log}")
