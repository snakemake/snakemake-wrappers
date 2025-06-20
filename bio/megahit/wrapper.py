"""Snakemake wrapper for megahit."""

__author__ = "Jie Zhu @alienzj, Filipe G. Vieira @fgvieira"
__copyright__ = "Copyright 2025, Jie Zhu, Filipe G. Vieira"
__email__ = "alienchuj@gmail.com"
__license__ = "MIT"

import tempfile
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_mem

# parse params
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
memory_requirements = get_mem(snakemake, out_unit="KiB") * 1024

# parse short reads
reads = snakemake.input.reads if hasattr(snakemake.input, "reads") else snakemake.input

input_arg = ""

# handle named inputs if available
if hasattr(snakemake.input, "r1") and hasattr(snakemake.input, "r2"):
    input_arg += f" -1 {snakemake.input.r1} -2 {snakemake.input.r2}"
elif len(reads) >= 2:
    input_arg += f" -1 {reads[0]} -2 {reads[1]}"

# handle interleaved reads if specified
if hasattr(snakemake.input, "interleaved"):
    input_arg += f" --12 {snakemake.input.interleaved}"
elif len(reads) >= 3 and not hasattr(snakemake.input, "r1"):
    input_arg += f" --12 {reads[2]}"

# handle additional reads if specified
if hasattr(snakemake.input, "unpaired"):
    input_arg += f" --read {snakemake.input.unpaired}"
elif len(reads) >= 4 and not hasattr(snakemake.input, "r1"):
    input_arg += f" --read {reads[3]}"

# run megahit
with tempfile.TemporaryDirectory() as tmpdir:
    output_tmpdir = Path(tmpdir) / "temp"

    shell(
        "megahit"
        " -t {snakemake.threads}"
        " -m {memory_requirements}"
        " -o {output_tmpdir}"
        " {input_arg}"
        " {extra}"
        " {log}"
    )

    # Ensure user can name each file according to their need
    output_mapping = {
        "contigs": f"{output_tmpdir}/final.contigs.fa",
        "json": f"{output_tmpdir}/options.json",
        "log": f"{output_tmpdir}/log",
    }
    for output_key, temp_file in output_mapping.items():
        output_path = snakemake.output.get(output_key)
        if output_path:
            shell("cp --verbose {temp_file:q} {output_path:q} {log}")
