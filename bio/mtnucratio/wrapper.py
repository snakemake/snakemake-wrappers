# coding: utf-8

"""Snakemake wrapper for MTNucRatioCalculator"""

from snakemake.shell import shell
from tempfile import TemporaryDirectory
from os.path import basename, realpath
from os import symlink

# Default mito chromosome name is set to 'MT'
chrom = snakemake.params.get("chrom", "MT")
log = snakemake.log_fmt_shell(
    stdout=True,
    stderr=True,
    append=True,
)
bam = str(snakemake.input)

# MTNucRatioCalculator does not let user chose
# output file names. Moving to a temporary directory:
with TemporaryDirectory() as tempdir:
    # Symlink input file to control output file names
    link_path = f"{tempdir}/{basename(bam)}"
    bam_path = realpath(bam)
    symlink(bam_path, link_path)

    # Run MTNucRatioCalculator
    shell("mtnucratio {link_path} {chrom} {log}")

    # Rename output files
    txt = snakemake.output.get("txt")
    if txt:
        shell("mv --verbose {link_path}.mtnucratio {txt} {log}")

    json = snakemake.output.get("json")
    if json:
        shell("mv --verbose {link_path}.mtnucratiomtnuc.json {json} {log}")
