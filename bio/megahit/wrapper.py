"""Snakemake wrapper for megahit."""

__author__ = "Jie Zhu @alienzj"
__copyright__ = "Copyright 2025, Jie Zhu"
__email__ = "alienchuj@gmail.com"
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
    else:
        output_file = snakemake.output[0]

    output_dir = os.path.split(output_file)[0]


# parse params
extra = snakemake.params.get("extra", "")
klist = snakemake.params.get("klist", "'21,29,39,59,79,99,119,141'")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

if hasattr(snakemake.resources, "mem_mb"):
    mem_bp = snakemake.resources.mem_mb * 1000000
    memory_requirements = f"{mem_bp}"
else:
    memory_requirements = "0.9"

if not os.path.exists(os.path.join(output_dir, "options.json")):
    # parse short reads
    if hasattr(snakemake.input, "reads"):
        reads = snakemake.input.reads
    else:
        reads = snakemake.input

    input_arg = " -1 {0} -2 {1} ".format(*reads)

    if len(reads) >= 3:
        input_arg += " --12 {2}".format(*reads)

        if len(reads) >= 4:
            input_arg += " --read {3}".format(*reads)

    shell("rm -rf {output_dir}")

    shell(
        "megahit "
        " -t {snakemake.threads} "
        " -m {memory_requirements} "
        " -o {output_dir} "
        " --k-list {klist} "
        " {input_arg} "
        " {extra} "
        " > {snakemake.log[0]} 2>&1 "
    )


else:
    # options.json file exitst already I restart from previous run

    shell(
        "echo '\n\nRestart MEGAHIT \n Remove pipline_state file copy files to force copy files if necessary.' >> {log[0]}"
    )

    shell("megahit " " --continue " " -o {output_dir} " " >> {snakemake.log[0]} 2>&1 ")

# Rename/ move output files

Output_key_mapping = {
    "contigs": "final.contigs.fa",
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
