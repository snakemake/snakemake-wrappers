__author__ = "Salomé Brunon"
__copyright__ = "Copyright 2024, Salomé Brunon"
__email__ = "salome.brunon@gmail.com"
__license__ = "CECILL-2.1"

from snakemake.shell import shell
from pathlib import Path

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

input_path = Path(snakemake.input[0])
if input_path.suffix == ".gz":
    input_path = input_path.with_suffix("")

if input_path.suffix in [".fastq", ".fq"]:
    input_flag = "--fastq "
elif input_path.suffix == ".bam":
    input_flag = "--bam "
else:
    input_flag = "--sequencing-summary-source "

outdir = Path(snakemake.output[0]).parent

shell("toulligqc {input_flag} {snakemake.input[0]} {extra} --force -n {outdir} {log}")
