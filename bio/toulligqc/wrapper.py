__author__ = "Salomé Brunon"
__copyright__ = "Copyright 2024, Salomé Brunon"
__email__ = "salome.brunon@gmail.com"
__license__ = "CECILL-2.1"

from snakemake.shell import shell

input_flag = "--sequencing-summary-source "
if snakemake.input[0].endswith(".fastq") or snakemake.input[0].endswith(".fastq.gz") or snakemake.input[0].endswith(".fasta") or snakemake.input[0].endswith(".fastq.gz"):
    input_flag = "--fastq "
if snakemake.input[0].endswith(".bam"):
    input_flag = "--bam "
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("toulligqc {extra} {input_flag} {snakemake.input} {log} -n toulligqc_demo --force")



