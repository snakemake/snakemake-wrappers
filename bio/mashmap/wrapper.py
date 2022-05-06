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
max_threads = snakemake.threads

# Handling input file types (either a fasta file, or a text file with a list of paths to fasta files)
ref = snakemake.input["ref"]
if ref.endswith(".txt"):
    ref = f"--refList {ref}"
elif ref.endswith(".gz"):
    ref = f"--ref <( gzip --decompress --stdout {ref} )"
    max_threads -= 1
else:
    ref = f"--ref {ref}"

if max_threads < 1:
    raise ValueError(
        "Reference fasta on-the-fly g-unzipping consumed one thread."
        f" Please increase the number of available threads by {1 - max_threads}."
    )


# Handling query file format (either a fastq file or a text file with a list of fastq files)
query = snakemake.input["query"]
if query.endswith(".txt"):
    query = f"--queryList {query}"
else:
    query = f"--query {query}"

shell(
    "mashmap "
    "{ref} "
    "{query} "
    "--output {snakemake.output} "
    "--threads {snakemake.threads} "
    "{extra} "
    "{log}"
)
