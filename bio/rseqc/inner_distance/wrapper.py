# coding: utf-8

"""Snakemake wrapper for RSeQC inner_distance.py"""

__author__ = "Thibault Dayris"
__mail__ = "thibault.dayris@gustaveroussy.fr"
__copyright__ = "Copyright 2024, Thibault Dayris"
__license__ = "MIT"

from tempfile import TemporaryDirectory
from snakemake import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

with TemporaryDirectory() as tempdir:
    shell(
        "inner_distance.py {extra} "
        "--input-file {snakemake.input.aln} "
        "--refgene {snakemake.input.refgene} "
        "--out-prefix {tempdir}/out "
        "{log} "
    )

    if snakemake.output.get("reads_inner_distance"):
        shell(
            "mv --verbose "
            "{tempdir}/out.inner_distance.txt "
            "{snakemake.output.reads_inner_distance} {log}"
        )

    if snakemake.output.get("pdf"):
        shell(
            "mv --verbose "
            "{tempdir}/out.inner_distance_plot.pdf "
            "{snakemake.output.pdf} {log}"
        )

    if snakemake.output.get("freq"):
        shell(
            "mv --verbose "
            "{tempdir}/out.inner_distance_freq.txt "
            "{snakemake.output.freq} {log}"
        )

    if snakemake.output.get("plot_r"):
        shell(
            "mv --verbose "
            "{tempdir}/out.inner_distance_plot.r "
            "{snakemake.output.plot_r} {log}"
        )
