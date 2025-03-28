__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2020, Christopher Schröder"
__email__ = "christopher.schroeder@tu-dortmund.de"
__license__ = "MIT"


from pathlib import Path
from snakemake.shell import shell


# Extract arguments.
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
sort_extra = snakemake.params.get("sort_extra", "")
samblaster_extra = snakemake.params.get("samblaster_extra", "")

index = snakemake.input.get("idx", "")
if isinstance(index, str):
    index = Path(index).stem
elif isinstance(index, list):
    index = Path(index[0]).stem


# Check inputs/arguments.
if not isinstance(snakemake.input.reads, str) and len(snakemake.input.reads) not in {
    1,
    2,
}:
    raise ValueError("input must have 1 (single-end) or 2 (paired-end) elements")

shell(
    "(bwa mem"
    " -t {snakemake.threads}"
    " {extra}"
    " {index}"
    " {snakemake.input.reads}"
    " | samblaster"
    " {samblaster_extra}"
    " | sambamba view -S -f bam /dev/stdin"
    " -t {snakemake.threads}"
    " | sambamba sort /dev/stdin"
    " -t {snakemake.threads}"
    " -o {snakemake.output.bam}"
    " {sort_extra}"
    ") {log}"
)
