"""Snakemake wrapper for subsampling reads from paired FASTQ files using seqtk."""

__author__ = "Fabian Kilpert"
__copyright__ = "Copyright 2020, Fabian Kilpert"
__email__ = "fkilpert@gmail.com"
__license__ = "MIT"


import os


log = snakemake.log_fmt_shell()


os.system(
    f"( "
    f"seqtk sample "
    f"-s {snakemake.params.seed} "
    f"{snakemake.input.f1} "
    f"{snakemake.params.n} "
    f"| pigz -9 -p {snakemake.threads} "
    f"> {snakemake.output.f1} "
    f"&& "
    f"seqtk sample "
    f"-s {snakemake.params.seed} "
    f"{snakemake.input.f2} "
    f"{snakemake.params.n} "
    f"| pigz -9 -p {snakemake.threads} "
    f"> {snakemake.output.f2} "
    f") {log} "
)
