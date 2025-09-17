# coding: utf-8

"""This snakemake wrappers runs pyEffGenomeSize.py"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2025, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake_wrapper_utils.snakemake import move_files, is_arg
from snakemake.shell import shell
from tempfile import TemporaryDirectory

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

# Optional IO files
bam = snakemake.input.get("bam")
if bam:
    extra += f" --bam '{bam}' --mosdepth "


# pyEffGenomeSize does not erase temporary files
# using a temporary directory to handle them:
with TemporaryDirectory() as tempdir:
    optional_output = {}
    thresholds = snakemake.output.get("thresholds")
    if thresholds:
        optional_output["thresholds"] = f"{tempdir}/snake_result.thresholds.bed"
        extra += " --saveIntermediates "

    regions = snakemake.output.get("regions")
    if regions:
        if not is_arg("--saveIntermediates", extra):
            extra += " --saveIntermediates "
        optional_output["regions"] = f"{tempdir}/snake_result.regions.bed.gz"

    intersect = snakemake.output.get("intersect")
    if intersect:
        optional_output["intersect"] = f"{tempdir}/snake_result.intersect.bed"

    shell(
        "pyEffGenomeSize.py {extra} "
        "--bed {snakemake.input.bed:q} "
        "--gtf {snakemake.input.gtf:q} "
        "--thread {snakemake.threads} "
        "--oprefix '{tempdir}/snake_result' "
        " > {snakemake.output.txt:q} "
        "{log} "
    )
    log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
    for move_cmd in move_files(snakemake, optional_output):
        shell("{move_cmd} {log}")
