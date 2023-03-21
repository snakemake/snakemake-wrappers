"""Snakemake wrapper for metaspades."""

__author__ = "Silas Kieser @silask"
__copyright__ = "Copyright 2021, Silas Kieser"
__email__ = "silas.kieser@gmail.com"
__license__ = "MIT"

import os, shutil
from snakemake.shell import shell


# infer output directory

if hasattr(snakemake.output, "dir"):
    output_dir = snakemake.output.dir

else:
    # get output_dir file from output
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

if hasattr(snakemake.resources, "mem_mb"):
    mem_gb = snakemake.resources.mem_mb // 1000
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

    input_arg = " --pe1-1 {0} --pe1-2 {1} ".format(*reads)

    if len(reads) >= 3:
        input_arg += " --pe1-m {2}".format(*reads)

        if len(reads) >= 4:
            input_arg += " --pe1-s {3}".format(*reads)

    # parse long reads
    for longread_name in ["pacbio", "nanopore"]:
        if hasattr(snakemake.input, longread_name):
            input_arg += " --{name} {}".format(name=longread_name, **snakemake.input)

    shell(
        "spades.py --meta "
        " --threads {snakemake.threads} "
        " {memory_requirements} "
        " -o {output_dir} "
        " -k {kmers} "
        " {input_arg} "
        " {extra} "
        " > {snakemake.log[0]} 2>&1 "
    )


else:
    # params.txt file exitst already I restart from previous run

    shell(
        "echo '\n\nRestart Spades \n Remove pipline_state file copy files to force copy files if necessary.' >> {log[0]}"
    )

    shell("rm -f {output_dir}/pipeline_state/stage_*_copy_files 2>> {log}")

    shell(
        "spades.py --meta "
        " --restart-from last "
        " --threads {threads} "
        " {memory_requirements} "
        " -o {output_dir} "
        " >> {snakemake.log[0]} 2>&1 "
    )


# Rename/ move output files

Output_key_mapping = {
    "contigs": "contigs.fasta",
    "scaffolds": "scaffolds.fasta",
    "graph": "assembly_graph_with_scaffolds.gfa",
}

has_named_output = False
for key in Output_key_mapping:
    if hasattr(snakemake.output, key):
        has_named_output = True
        file_produced = os.path.join(output_dir, Output_key_mapping[key])
        file_renamed = getattr(snakemake.output, key)

        if file_produced != file_renamed:
            shutil.move(file_produced, file_renamed)


if not has_named_output:
    file_produced = os.path.join(output_dir, "contigs.fasta")
    file_renamed = snakemake.output[0]

    if file_produced != file_renamed:
        shutil.move(file_produced, file_renamed)
