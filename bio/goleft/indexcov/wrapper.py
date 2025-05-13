# coding: utf-8

__author__ = "Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__copyright__ = "Copyright 2024, Thibault Dayris"
__license__ = "MIT"

from pathlib import Path
from tempfile import TemporaryDirectory
from snakemake import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

with TemporaryDirectory() as tempdir:
    shell(
        "goleft indexcov "
        "{extra} "
        "--directory {tempdir}/out "
        "--fai {snakemake.input.fai} "
        "{snakemake.input.aln} "
        "{log} "
    )

    if snakemake.output.get("ped"):
        shell(
            "mv --verbose "
            "{tempdir}/out/out-indexcov.ped "
            "{snakemake.output.ped} "
            "{log} "
        )

    if snakemake.output.get("roc"):
        shell(
            "mv --verbose "
            "{tempdir}/out/out-indexcov.roc "
            "{snakemake.output.roc} "
            "{log} "
        )

    if snakemake.output.get("bed"):
        shell(
            "mv --verbose "
            "{tempdir}/out/out-indexcov.bed.gz "
            "{snakemake.output.bed} "
            "{log} "
        )

    # Number of files withing tempdir output
    # is defined by user command line parameters
    # and/or chromosomes present in the fasta index
    if snakemake.output.get("html"):
        # Not created automatically by Snakemake
        Path(snakemake.output.html).mkdir(parents=True, exist_ok=True)
        shell("mv --verbose {tempdir}/out/* {snakemake.output.html} {log}")
