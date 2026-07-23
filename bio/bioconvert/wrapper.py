# coding: utf-8

"""Snakemake wrapper for bioconvert"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2025, Thibault Dayris"
__license__ = "MIT"


from snakemake.shell import shell
from tempfile import TemporaryDirectory

extra = snakemake.params.get("extra", "")
converter = snakemake.params.get("converter", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Some optional parameters have to be provided, but implicit
# convertion (when user does not provide any converter) may
# use odd conversion paths, especially when using `--allow-indirect-convertion`
# We're setting optional parameters only when converter is provided.
if converter:
    multi_threaded_commands = {
        "bam2bedgraph",
        "bam2cram",
        "bam2sam",
        "bz22gz",
        "cram2bam",
        "cram2fasta",
        "cram2fastq",
        "cram2sam",
        "dsrc2gz",
        "fast52pod5",
        "fastq2fasta",
        "gz2bz2",
        "gz2dsrc",
        "sam2bam",
        "sam2cram",
    }
    if converter in multi_threaded_commands:
        extra += f" --threads {snakemake.threads}"

    commands_expecting_reference = {
        "bam2cram",
        "cram2bam",
        "cram2fasta",
        "cram2fastq",
        "cram2sam",
        "sam2cram",
    }
    if converter in commands_expecting_reference:
        extra += f" --reference '{snakemake.input.ref}'"

shell("bioconvert {converter} {extra} {snakemake.input[0]} {snakemake.output[0]} {log}")
