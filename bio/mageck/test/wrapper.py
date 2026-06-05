# coding: utf-8

"""Snakemake wrapper for MaGeCK Test"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2026, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from pathlib import Path
from tempfile import TemporaryDirectory
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import move_files

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

cnv = snakemake.input.get("cnv", "")
if cnv:
    cnv = f"--cnv-norm {cnv} "

with TemporaryDirectory() as tempdir:
    outfile_mapping = {
        "rra": f"{tempdir}.gene_summary.txt",
        "r_script": f"{tempdir}.R",
        "rmd_report": f"{tempdir}.report.Rmd",
        "sgrna_summary": f"{tempdir}.sgrna_summary.txt",
        "sweave": f"{tempdir}_summary.Rnw",
        "logs": f"{tempdir}.log",
    }

    pdf = snakemake.output.get("pdf")
    if pdf:
        extra += " --pdf-report "
        outfile_mapping["pdf"] = f"{tempdir}.pdf"

    normalized = snakemake.output.get("normalized")
    if normalized:
        extra += " --normcounts-to-file "
        outfile_mapping["normalized"] = f"{tempdir}.normalized.txt"

    shell(
        "mageck test {extra} --count-table {snakemake.input.counts} "
        "--output-prefix {tempdir} {cnv} {log} "
        " && tree {tempdir}* {log} "
        " && ls {tempdir}* {log} "
    )

    for move_cmd in move_files(snakemake, outfile_mapping):
        shell("{move_cmd} {log}")
