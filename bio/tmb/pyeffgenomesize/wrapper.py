# coding: utf-8

"""This snakemake wrappers runs pyEffGenomeSize.py"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2025, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

# Optional IO files
bam = snakemake.input.get("bam")
if bam:
    extra += f" --bam '{bam}' --mosdepth "

thresholds = snakemake.output.get("thresholds")
regions = snakemake.output.get("regions")
if thresholds or regions:
    extra += " --saveIntermediates "

# pyEffGenomeSize does not erase temporary files
# using a temporary directory to handle them:
with TemporaryDirectory() as tempdir:
    shell(
        "pyEffGenomeSize.py {extra} "
        "--bed {snakemake.input.bed:q} "
        "--gtf {snakemake.input.gtf:q} "
        "--thread {snakemake.threads} "
        "--oprefix '{tempdir}/snake_result' "
        " > {snakemake.output.txt:q} "
        "{log} "
    )

    # Moving optional output files
    log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
    intersect = snakemake.output.get("intersect")
    if intersect:
        shell("mv --verbose {tempdir}/snake_result.intersect.bed {intersect} {log}")

    if thresholds:
        shell("mv --verbose {tempdir}/snake_result.thresholds.bed {thresholds} {log}")

    if regions:
        shell("mv --verbose {tempdir}/snake_result.regions.bed.gz {regions} {log}")
