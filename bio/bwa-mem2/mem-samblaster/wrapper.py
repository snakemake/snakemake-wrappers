__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2020, Christopher Schröder"
__email__ = "christopher.schroeder@tu-dortmund.de"
__license__ = "MIT"


from os import path

from snakemake.shell import shell


# Extract arguments.
extra = snakemake.params.get("extra", "")
sort_extra = snakemake.params.get("sort_extra", "")
samblaster_extra = snakemake.params.get("samblaster_extra", "")

index = None
if "index" in snakemake.params.keys():
    index = snakemake.params["index"]
elif "index" in snakemake.input.keys():
    index = path.splitext(snakemake.input["index"])[0]
else:
    raise ValueError("Could not find BWA index prefix")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Check inputs/arguments.
if not isinstance(snakemake.input.reads, str) and len(snakemake.input.reads) not in {
    1,
    2,
}:
    raise ValueError("input must have 1 (single-end) or 2 (paired-end) elements")

shell(
    "(bwa-mem2 mem"
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
