"""Snakemake wrapper for megahit."""

__author__ = "Jie Zhu @alienzj"
__copyright__ = "Copyright 2025, Jie Zhu"
__email__ = "alienchuj@gmail.com"
__license__ = "MIT"

import os, tempfile, shutil
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_mem

# get output_dir and files from output
output_dir = os.path.split(snakemake.output[0])[0]
contigs_file = snakemake.output.get("contigs", os.path.join(output_dir, "contigs.fa"))
contigs_file_original = os.path.join(output_dir, "final.contigs.fa")
options_file = snakemake.output.get("options", os.path.join(output_dir, "options.json"))
log_file = snakemake.output.get("log", os.path.join(output_dir, "log"))

# parse params
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
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


with tempfile.TemporaryDirectory() as temp_dir:
    output_temp_dir = os.path.join(temp_dir, "temp")

    shell(
        "megahit "
        " -t {snakemake.threads} "
        " -m {memory_requirements} "
        " -o {output_temp_dir} "
        " {input_arg} "
        " {extra} "
        " {log}"
    )

    if os.path.exists(os.path.join(output_temp_dir, "done")):
        shell("rm -rf {output_dir}")
        shutil.move(output_temp_dir, output_dir)

        if (
            os.path.exists(contigs_file_original)
            and os.path.exists(options_file)
            and os.path.exists(log_file)
        ):
            shutil.move(contigs_file_original, contigs_file)
