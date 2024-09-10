__author__ = "Salomé Brunon"
__copyright__ = "Copyright 2024, Salomé Brunon"
__email__ = "salome.brunon@gmail.com"
__license__ = "CECILL-2.1"

from snakemake.shell import shell
from pathlib import Path

input_path = Path(snakemake.input[0])
if input_path.suffix in [".fastq", ".fastq.gz", ".fasta", ".fasta.gz"]:
    input_flag = "--fastq "
elif input_path.suffix == ".bam":
    input_flag = "--bam "
else:
    input_flag = "--sequencing-summary-source "

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("toulligqc {extra} {input_flag} {snakemake.input} {log} -n toulligqc_demo --force")





