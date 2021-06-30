"""Snakemake wrapper for metaspades."""

__author__ = "Silas Kieser @silask"
__copyright__ = "Copyright 2021, Silas Kieser"
__email__ = "silas.kieser@gmail.com"
__license__ = "MIT"

import os
from snakemake.shell import shell

output_contigs = snakemake.output[0]

output_dir, output_file = os.path.split(output_contigs)
if not ((output_file == "contigs.fasta") or (output_file == "scaffolds.fasta")):
    raise Exception(
        "First output file should be folder/contigs.fasta or folder/scaffolds.fasta"
    )

    # parse params
    extra = snakemake.params.get("extra", "")
    kmers = snakemake.params.get("k", "'auto'")

    log = snakemake.log_fmt_shell(stdout=False, stderr=True)

    # parse reads

    if hasattr(snakemake.input, "reads"):
        reads = snakemake.input.reads
    else:
        reads = snakemake.input

    assert (
        len(reads) > 1
    ), "Metaspades needs a paired end library. This means you should supply at least 2 fastq files in the rule input."

    input += " --pe1-1 {0} --pe1-2 {1} ".format(*reads)

    if len(reads) >= 3:
        input += " --pe1-m {2}".format(*reads)

        if len(reads) >= 4:
            input += " --pe1-s {3}".format(*reads)

    # parse long reads
    for longread_name in ["pacbio", "nanopore"]:
        if hasattr(snakemake.input, longread_name):
            input += " --{name} {}".format(name=longread_name, **snakemake.input)


if not os.path.exists(os.path.join(output_folder, "params.txt")):

    shell(
        "spades.py --meta "
        " --threads {threads} "
        " --memory {resources.mem_mb}000 "
        " -o {output_dir} "
        " -k {kmers} "
        " {input} "
        " {extra} "
        " > {log[0]} 2>&1 "
    )


else:
    # params.txt file exitst already I restart from previous run

    shell("echo '\n\nRestart Spades \n' >> {log[0]}")

    shell(
        "spades.py --meta "
        " --threads {threads} "
        " --memory {resources.mem_mb}000 "
        " -o {output_dir} "
        " >> {log[0]} 2>&1 "
    )
