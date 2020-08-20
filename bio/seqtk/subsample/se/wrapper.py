"""Snakemake wrapper for subsampling reads from FASTQ file using seqtk."""

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
    f"{snakemake.input} "
    f"{snakemake.params.n} "
    f"| pigz -9 -p {snakemake.threads} "
    f"> {snakemake.output} "
    f") {log} "
)
