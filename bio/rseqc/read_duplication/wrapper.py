# coding: utf-8

"""Snakemake wrapper for RSeQC read_duplication.py"""

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
        "read_duplication.py {extra} "
        "--input-file {snakemake.input} "
        "--out-prefix {tempdir}/out "
        "{log} "
    )

    if "pos" in snakemake.output.keys():
        shell(
            "mv --verbose "
            "{tempdir}/out.pos.DupRate.xls "
            "{snakemake.output.pos} "
            "{log} "
        )

    if "seq" in snakemake.output.keys():
        shell(
            "mv --verbose "
            "{tempdir}/out.seq.DupRate.xls "
            "{snakemake.output.seq} "
            "{log} "
        )

    if "plot_r" in snakemake.output.keys():
        shell(
            "mv --verbose "
            "{tempdir}/out.DupRate_plot.r "
            "{snakemake.output.plot_r} "
            "{log} "
        )

    if "pdf" in snakemake.output.keys():
        shell(
            "mv --verbose "
            "{tempdir}/out.DupRate_plot.pdf "
            "{snakemake.output.pdf} "
            "{log} "
        )
