__author__ = "Artur Gomes"
__copyright__ = "Copyright 2026, Artur Gomes"
__email__ = "arafaelogomes@gmail.com"
__license__ = "MIT"

import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

if hasattr(snakemake.resources, "mem_mb"):
    mem_gb = snakemake.resources.mem_mb // 1000
    extra += f" --memory {mem_gb}"

output_dir = snakemake.output.get("dir")
if output_dir is None:
    output_file = (
        snakemake.output.get("contigs")
        or snakemake.output.get("scaffolds")
        or snakemake.output[0]
    )
    output_dir = os.path.dirname(output_file) or "."

os.makedirs(output_dir, exist_ok=True)

input_arg = ""

seq_types = {
    "nano-raw": "--nano-raw",
    "nano-corr": "--nano-corr",
    "nano-hq": "--nano-hq",
    "pacbio-raw": "--pacbio-raw",
    "pacbio-corr": "--pacbio-corr",
    "pacbio-hifi": "--pacbio-hifi",
}

param_seq_type = snakemake.params.get("seq_type", "")
if param_seq_type:
    if param_seq_type in seq_types:
        input_arg += f" {seq_types[param_seq_type]}"
    else:
        raise ValueError(
            f"Invalid seq_type: {param_seq_type}. Must be one of: {', '.join(seq_types.keys())}"
        )

reads = snakemake.input.get("reads")
if reads:
    if isinstance(reads, list):
        reads = " ".join(reads)
    input_arg += f" {reads}"

if snakemake.params.get("meta"):
    extra += " --meta"

if snakemake.params.get("keep_haplotypes"):
    extra += " --keep-haplotypes"

if snakemake.params.get("no_alt_contigs"):
    extra += " --no-alt-contigs"

if snakemake.params.get("scaffold"):
    extra += " --scaffold"

shell(
    "flye"
    " --threads {snakemake.threads}"
    " {extra}"
    " {input_arg}"
    " -o {output_dir}"
    " {log}"
)
