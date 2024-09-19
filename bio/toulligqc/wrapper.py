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

if input_path.suffix in [".fastq", ".fastq", ".fas", ".fq"]:
    input_flag = "--fastq "
    outdir_flag = "-n toulligqc_fastq"
elif input_path.suffix == ".bam":
    input_flag = "--bam "
    outdir_flag = "-n toulligqc_bam"
else:
    input_flag = "--sequencing-summary-source "
    outdir_flag = "-n toulligqc_sequencing_summary"

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("toulligqc {extra} {input_flag} {snakemake.input} {log} {outdir_flag} --force")





