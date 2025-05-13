# coding: utf-8

"""Snakemake wrapper for RSeQC read_GC.py"""

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
        "read_GC.py {extra} "
        "--input-file {snakemake.input} "
        "--out-prefix {tempdir}/out "
        "{log} "
    )

    if "xls" in snakemake.output.keys():
        shell(
            "mv --verbose " "{tempdir}/out.GC.xls " "{snakemake.output.xls} " "{log} "
        )

    if "plot_r" in snakemake.output.keys():
        shell(
            "mv --verbose "
            "{tempdir}/out.GC_plot.r "
            "{snakemake.output.plot_r} "
            "{log} "
        )

    if "pdf" in snakemake.output.keys():
        shell(
            "mv --verbose "
            "{tempdir}/out.GC_plot.pdf "
            "{snakemake.output.pdf} "
            "{log} "
        )
