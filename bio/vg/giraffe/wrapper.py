__author__ = "Felix Mölder"
__copyright__ = "Copyright 2024, Felix Mölder"
__email__ = "felix.moelder@uk-essen.de"
__license__ = "MIT"


import tempfile
from os import path
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts
from snakemake_wrapper_utils.samtools import get_samtools_opts


# Extract arguments.
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
sort = snakemake.params.get("sorting", "none")
sort_order = snakemake.params.get("sort_order", "coordinate")
sort_extra = snakemake.params.get("sort_extra", "")
samtools_opts = get_samtools_opts(snakemake, param_name="sort_extra")
java_opts = get_java_opts(snakemake)

# Check inputs/arguments.
if not isinstance(snakemake.input.reads, str) and len(snakemake.input.reads) not in {
    1,
    2,
}:
    raise ValueError("input must have 1 (single-end) or 2 (paired-end) elements")

reads = (
    snakemake.input.reads
    if isinstance(snakemake.input.reads, str)
    else " -f ".join(snakemake.input.reads)
)

input_cmd = ""
if snakemake.input.get("hapl", ""):
    input_cmd += f" --haplotype-name {snakemake.input.hapl}"
if snakemake.input.get("kmers", ""):
    input_cmd += f" --kff-name {snakemake.input.kmers}"

if sort_order not in {"coordinate", "queryname"}:
    raise ValueError("Unexpected value for sort_order ({})".format(sort_order))


# Determine which pipe command to use for converting to bam or sorting.
if sort == "none":
    # Simply convert to bam using samtools view.
    pipe_cmd = f"samtools view {samtools_opts}"
elif sort == "samtools":
    # Add name flag if needed.
    if sort_order == "queryname":
        sort_extra += " -n"
    # Sort alignments using samtools sort.
    pipe_cmd = "samtools sort {samtools_opts} {sort_extra} -T {tmpdir}"
elif sort == "fgbio":
    if sort_order == "queryname":
        sort_extra += " -s Queryname"
    pipe_cmd = "fgbio SortBam -i /dev/stdin -o {snakemake.output.bam} {sort_extra}"
elif sort == "picard":
    # Sort alignments using picard SortSam.
    pipe_cmd = "picard SortSam {java_opts} {sort_extra} --INPUT /dev/stdin --TMP_DIR {tmpdir} --SORT_ORDER {sort_order} --OUTPUT {snakemake.output[0]}"
else:
    raise ValueError(f"Unexpected value for params.sort ({sort})")


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(vg giraffe -p "
        " -t {snakemake.threads}"
        " -Z {snakemake.input.graph}"
        " {input_cmd}"
        " -f {reads}"
        " --output-format BAM"
        " {extra}"
        " | " + pipe_cmd + ") {log}"
    )
