__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2020, Christopher Schröder"
__email__ = "christopher.schroeder@tu-dortmund.de"
__license__ = "MIT"


import os
from os import path


# Extract arguments.
extra = snakemake.params.get("extra", "")
sort_extra = snakemake.params.get("sort_extra", "")
samblaster_extra = snakemake.params.get("samblaster_extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Check inputs/arguments.
if not isinstance(snakemake.input.reads, str) and len(snakemake.input.reads) not in {
    1,
    2,
}:
    raise ValueError("input must have 1 (single-end) or 2 (paired-end) elements")

os.system(
    f"(bwa-mem2 mem"
    f" -t {snakemake.threads}"
    f" {extra}"
    f" {snakemake.params.index}"
    f" {snakemake.input.reads}"
    f" | samblaster"
    f" {samblaster_extra}"
    f" | sambamba view -S -f bam /dev/stdin"
    f" -t {snakemake.threads}"
    f" | sambamba sort /dev/stdin"
    f" -t {snakemake.threads}"
    f" -o {snakemake.output.bam}"
    f" {sort_extra}"
    f") {log}"
)
