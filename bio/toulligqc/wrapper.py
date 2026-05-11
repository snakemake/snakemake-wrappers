__author__ = "Salomé Brunon"
__copyright__ = "Copyright 2024, Salomé Brunon"
__email__ = "salome.brunon@gmail.com"
__license__ = "CECILL-2.1"

from snakemake.shell import shell
from pathlib import Path
from snakemake_wrapper_utils.snakemake import get_format

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

in_format = get_format(snakemake.input[0])
if in_format in ["fastq", "bam"]:
    input_flag = f"--{in_format}"
else:
    input_flag = "--sequencing-summary-source "

outdir = Path(snakemake.output[0]).parent

shell("toulligqc {input_flag} {snakemake.input[0]} {extra} --force -n {outdir} {log}")
