"""Snakemake wrapper for Trinity."""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2018, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

import os
from os import path

extra = snakemake.params.get("extra", "")
max_memory = snakemake.params.get("max_memory", "10G")

# allow multiple input files for single assembly
left = snakemake.input.get("left")
assert left is not None, "input-> left is a required input parameter"
left = (
    [snakemake.input.left]
    if isinstance(snakemake.input.left, str)
    else snakemake.input.left
)
right = snakemake.input.get("right")
if right:
    right = (
        [snakemake.input.right]
        if isinstance(snakemake.input.right, str)
        else snakemake.input.right
    )
    assert len(left) >= len(
        right
    ), "left input needs to contain at least the same number of files as the right input (can contain additional, single-end files)"
    input_str_left = " --left " + ",".join(left)
    input_str_right = " --right " + ",".join(right)
else:
    input_str_left = " --single " + ",".join(left)
    input_str_right = ""

input_cmd = " ".join([input_str_left, input_str_right])

# infer seqtype from input files:
seqtype = snakemake.params.get("seqtype")
if not seqtype:
    if "fq" in left[0] or "fastq" in left[0]:
        seqtype = "fq"
    elif "fa" in left[0] or "fasta" in left[0]:
        seqtype = "fa"
    else:  # assertion is redundant - warning or error instead?
        assert (
            seqtype is not None
        ), "cannot infer 'fq' or 'fa' seqtype from input files. Please specify 'fq' or 'fa' in 'seqtype' parameter"

outdir = path.dirname(snakemake.output[0])
assert "trinity" in outdir, "output directory name must contain 'trinity'"

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

os.system(
    f"Trinity {input_cmd} --CPU {snakemake.threads} "
    f" --max_memory {max_memory} --seqType {seqtype} "
    f" --output {outdir} {snakemake.params.extra} "
    f" {log}"
)
