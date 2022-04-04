__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from os import path
import re
import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts
from snakemake_wrapper_utils.java import get_java_opts


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
samtools_opts = samtools_opts = get_samtools_opts(snakemake)
java_opts = get_java_opts(snakemake)


sort = snakemake.params.get("sorting", "none")
sort_order = snakemake.params.get("sort_order", "coordinate")
sort_extra = snakemake.params.get("sort_extra", "")


n = len(snakemake.input.reads)
assert (
    n == 1 or n == 2
), "input->reads must have 1 (single-end) or 2 (paired-end) elements."

if n == 1:
    reads = "-1 {}".format(*snakemake.input.reads)
else:
    reads = "-1 {} -2 {}".format(*snakemake.input.reads)


index = snakemake.input.idx
if isinstance(index, str):
    index = path.splitext(snakemake.input.idx)[0]
else:
    index = path.splitext(snakemake.input.idx[0])[0]


if sort_order not in {"coordinate", "queryname"}:
    raise ValueError("Unexpected value for sort_order ({})".format(sort_order))

# Determine which pipe command to use for converting to bam or sorting.
if sort == "none":
    # Simply convert to bam using samtools view.
    pipe_cmd = "samtools view {samtools_opts} {sort_extra} -"

elif sort == "samtools":
    # Add name flag if needed.
    if sort_order == "queryname":
        sort_extra += " -n"

    # Sort alignments using samtools sort.
    pipe_cmd = "samtools sort {samtools_opts} {sort_extra} -"

elif sort == "picard":
    # Sort alignments using picard SortSam.
    pipe_cmd = (
        "picard SortSam {java_opts} {sort_extra} --INPUT /dev/stdin"
        " --OUTPUT {snakemake.output[0]} --SORT_ORDER {sort_order} --TMP_DIR {tmpdir}"
    )
else:
    raise ValueError("Unexpected value for params.sort ({})".format(sort))


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(dragen-os"
        " --num-threads {snakemake.threads}"
        " -r {snakemake.input.idx}"
        " {reads}"
        " {extra}"
        " | " + pipe_cmd + ") {log}"
    )
