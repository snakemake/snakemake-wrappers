#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Snakemake wrapper for gentrome and decoy sequences acquisition"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2022, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True, append=True)
required_thread_nb = 1

genome = snakemake.input["genome"]
if genome.endswith(".gz"):
    genome = f"<( gzip --stdout --decompress {genome} )"
    required_thread_nb += 1  # Add a thread for gzip uncompression
elif genome.endswith(".bz2"):
    genome = f"<( bzip2 --stdout --decompress {genome} )"
    required_thread_nb += 1  # Add a thread for bzip2 uncompression

if snakemake.threads < required_thread_nb:
    raise ValueError(
        f"Salmon decoy wrapper requires exactly {required_thread_nb} threads, "
        f"but only {snakemake.threads} were provided"
    )

sequences = [
    snakemake.input["transcriptome"],
    snakemake.input["genome"],
    snakemake.output["gentrome"],
]
if all(fasta.endswith(".gz") for fasta in sequences):
    # Then all input sequences are gzipped. The output will also be gzipped.
    pass
elif all(fasta.endswith(".bz2") for fasta in sequences):
    # Then all input sequences are bgzipped. The output will also be bgzipped.
    pass
elif all(fasta.endswith((".fa", ".fna", ".fasta")) for fasta in sequences):
    # Then all input sequences are raw fasta. The output will also be raw fasta.
    pass
else:
    raise ValueError(
        "Mixed compression status: Either all fasta sequences are compressed "
        "with the *same* compression algorithm, or none of them are compressed."
    )

# Gathering decoy sequences names
# Sed command works as follow:
# -n       = do not print all lines
# s/ .*//g = Remove anything after spaces. (remove comments)
# s/>//p  = Remove '>' character at the begining of sequence names. Print names.
shell("( sed -n 's/ .*//g;s/>//p' {genome} ) > {snakemake.output.decoys} {log}")

# Building big gentrome file
shell(
    "cat {snakemake.input.transcriptome} {snakemake.input.genome} "
    "> {snakemake.output.gentrome} {log}"
)
