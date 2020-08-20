"""Snakemake wrapper for subsampling reads from FASTQ file using seqtk."""

__author__ = "Fabian Kilpert"
__copyright__ = "Copyright 2020, Fabian Kilpert"
__email__ = "fkilpert@gmail.com"
__license__ = "MIT"


import os


log = snakemake.log_fmt_shell()


os.system(
    f"( "
    "seqtk sample "
    "-s {snakemake.params.seed} "
    "{snakemake.input} "
    "{snakemake.params.n} "
    "| pigz -9 -p {snakemake.threads} "
    "> {snakemake.output} "
    ") {log} "
)
