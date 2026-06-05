# coding: utf-8

"""Snakemake wrapper for MaGeCK MLE"""

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
    extra += f" --cnv-norm {cnv}"

design = snakemake.input.get("design", "")
if design:
    extra += f" --design-matrix {design}"


with TemporaryDirectory() as tempdir:
    temp_prefix = f"{tempdir}/snake_out"
    outfile_mapping = {
        "mle": f"{temp_prefix}.gene_summary.txt",
        "mle_log": f"{temp_prefix}.log",
        "sgrna": f"{temp_prefix}.sgrna_summary.txt",
    }

    shell(
        "mageck mle {extra} --count-table {snakemake.input.counts} "
        "--output-prefix {temp_prefix} {log} "
    )

    for move_cmd in move_files(snakemake, outfile_mapping):
        shell("{move_cmd} {log}")
