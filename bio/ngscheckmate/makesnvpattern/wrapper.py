# coding: utf-8

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2024, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory
from os.path import commonprefix

# Optional parameters
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
extra = snakemake.params.get("extra", "")

index = commonprefix(snakemake.input.bowtie).rstrip(".")

with TemporaryDirectory() as tempdir:
    shell(
        "makesnvpattern.pl "
        "{snakemake.input.bed} "
        "{snakemake.input.fasta} "
        "{index} {tempdir} snake_out {log}"
    )

    # Ensure user can name each file according to their need
    bowtieout = snakemake.output.get("bowtie")
    if bowtieout:
        shell("mv --verbose '{tempdir}/snake_out.bowtieout' {bowtieout} {log}")

    fasta = snakemake.output.get("fasta")
    if fasta:
        shell("mv --verbose '{tempdir}/snake_out.fasta' {fasta} {log}")

    ntm = snakemake.output.get("ntm")
    if ntm:
        shell("mv --verbose '{tempdir}/snake_out.ntm' {ntm} {log}")

    pattern = snakemake.output.get("pattern")
    if pattern:
        shell("mv --verbose '{tempdir}/snake_out.pt' {pattern} {log}")

    pattern_text = snakemake.output.get("pattern_text")
    if pattern_text:
        shell("mv --verbose '{tempdir}/snake_out.pt-txt' {pattern_text} {log}")

    pattern_sorted = snakemake.output.get("pattern_sorted")
    if pattern_sorted:
        shell("mv --verbose '{tempdir}/snake_out.pt-txt.sorted' {pattern_sorted} {log}")

    text = snakemake.output.get("text")
    if text:
        shell("mv --verbose '{tempdir}/snake_out.txt' {text} {log}")

    uniq = snakemake.output.get("uniq")
    if uniq:
        shell("mv --verbose '{tempdir}/snake_out.uniq.txt' {uniq} {log}")

    txt_sorted = snakemake.output.get("txt_sorted")
    if txt_sorted:
        shell("mv --verbose '{tempdir}/snake_out.uniq.txt.sorted' {txt_sorted} {log}")
