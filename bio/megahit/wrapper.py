"""Snakemake wrapper for megahit."""

__author__ = "Jie Zhu @alienzj, Filipe G. Vieira @fgvieira"
__copyright__ = "Copyright 2025, Jie Zhu, Filipe G. Vieira"
__email__ = "alienchuj@gmail.com"
__license__ = "MIT"

import os, tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_mem

# parse params
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
memory_requirements = get_mem(snakemake, out_unit="KiB") * 1024

# parse short reads
if hasattr(snakemake.input, "reads"):
    reads = snakemake.input.reads
else:
    reads = snakemake.input

input_arg = ""

# handle named inputs if available
if hasattr(snakemake.input, "r1") and hasattr(snakemake.input, "r2"):
    input_arg += " -1 {} -2 {} ".format(snakemake.input.r1, snakemake.input.r2)
elif len(reads) >= 2:
    input_arg += " -1 {} -2 {} ".format(reads[0], reads[1])

# handle interleaved reads if specified
if hasattr(snakemake.input, "interleaved"):
    input_arg += " --12 {} ".format(snakemake.input.interleaved)
elif len(reads) >= 3 and not hasattr(snakemake.input, "r1"):
    input_arg += " --12 {} ".format(reads[2])

# handle additional reads if specified
if hasattr(snakemake.input, "unpaired"):
    input_arg += " --read {} ".format(snakemake.input.unpaired)
elif len(reads) >= 4 and not hasattr(snakemake.input, "r1"):
    input_arg += " --read {} ".format(reads[3])

# run megahit
output_dir = os.path.dirname(snakemake.output.get("contigs"))
with tempfile.TemporaryDirectory(dir=os.path.dirname(output_dir)) as temp_dir:
    output_temp_dir = os.path.join(temp_dir, "temp")

    shell(
        "megahit "
        " -t {snakemake.threads} "
        " -m {memory_requirements} "
        " -o {output_temp_dir} "
        " {input_arg} "
        " {extra} "
        " {log} "
    )

    # Ensure user can name each file according to their need
    output_mapping = {
        "contigs": f"{output_temp_dir}/final.contigs.fa",
        "json": f"{output_temp_dir}/options.json",
        "log": f"{output_temp_dir}/log",
    }
    for output_key, temp_file in output_mapping.items():
        output_path = snakemake.output.get(output_key)
        if output_path:
            shell("mv --verbose {temp_file:q} {output_path:q} {log}")
