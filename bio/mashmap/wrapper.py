#!/usr/bin/python3.8
# coding: utf-8

""" Snakemake wrapper for MashMap """

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2022, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

# Handling input file types (either a fasta file, or a text file with a list of paths to fasta files)
ref = snakemake.input["ref"]
if ref.endswith((".fa", ".fna", ".fasta")):
    ref = f"--ref {ref}"
else:
    ref = f"--refList {ref}"

shell(
    "mashmap "
    "{ref} "
    "--query {snakemake.input.query} "
    "--output {snakemake.output} "
    "--threads {snakemake.threads} "
    "{extra} "
    "{log}"
)