"""Snakemake wrapper for metaspades."""

__author__ = "Silas Kieser @silask"
__copyright__ = "Copyright 2021, Silas Kieser"
__email__ = "silas.kieser@gmail.com"
__license__ = "MIT"

import os, shutil
from snakemake.shell import shell


# infer output directory

if hasattr(snakemake.params, "output_dir"):
    output_dir = snakemake.params.output_dir
    os.makedirs(output_dir, exists_ok=True)

    need_copy_output_files = True
else:
    # get output_dir file from output
    need_copy_output_files = False
    if hasattr(snakemake.output, "contigs"):
        output_file = snakemake.output.contigs
    elif hasattr(snakemake.output, "scaffolds"):
        output_file = snakemake.output.scaffolds
    else:
        output_file = snakemake.output[0]

    output_dir = os.path.split(output_file)[0]


# parse params
extra = snakemake.params.get("extra", "")
kmers = snakemake.params.get("k", "'auto'")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

if hasattr(snakemake.resources,'mem_mb'):
    mem_gb= snakemake.resources.mem_mb // 1000
    memory_requirements = f" --memory {mem_gb}"
else:
    memory_requirements = ""

if not os.path.exists(os.path.join(output_dir, "params.txt")):

    # parse short reads
    if hasattr(snakemake.input, "reads"):
        reads = snakemake.input.reads
    else:
        reads = snakemake.input

    assert (
        len(reads) > 1
    ), "Metaspades needs a paired end library. This means you should supply at least 2 fastq files in the rule input."

    assert (
        type(reads[0]) == str
    ), f"Metaspades allows only 1 library. Therefore reads need to be strings got {reads}"

    input += " --pe1-1 {0} --pe1-2 {1} ".format(*reads)

    if len(reads) >= 3:
        input += " --pe1-m {2}".format(*reads)

        if len(reads) >= 4:
            input += " --pe1-s {3}".format(*reads)

    # parse long reads
    for longread_name in ["pacbio", "nanopore"]:
        if hasattr(snakemake.input, longread_name):
            input += " --{name} {}".format(name=longread_name, **snakemake.input)

    shell(
        "spades.py --meta "
        " --threads {threads} "
        " {memory_requirements} "
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
        " --restart-from last "
        " --threads {threads} "
        " {memory_requirements} "
        " -o {output_dir} "
        " >> {log[0]} 2>&1 "
    )


if need_copy_output_files:

    if hasattr(snakemake.output, "scaffolds"):
        shutil.copy(
            os.path.join(output_dir, "scaffolds.fasta"), snakemake.output.scaffolds
        )
    if hasattr(snakemake.output, "contigs"):
        output_contigs = snakemake.output.contigs
    else:
        output_contigs = snakemake.output[0]

    shutil.copy(os.path.join(output_dir, "contigs.fasta"), output_contigs)
