"""Snakemake wrapper for PLASS Protein-Level Assembler."""

__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2018, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

# allow multiple input files for single assembly
left = snakemake.input.get("left")
single = snakemake.input.get("single")
assert (
    left is not None or single is not None
), "please check read inputs: either left/right or single read file inputs are required"
if left:
    left = (
        [snakemake.input.left]
        if isinstance(snakemake.input.left, str)
        else snakemake.input.left
    )
    right = snakemake.input.get("right")
    assert (
        right is not None
    ), "please input 'right' reads or specify that the reads are 'single'"
    right = (
        [snakemake.input.right]
        if isinstance(snakemake.input.right, str)
        else snakemake.input.right
    )
    assert len(left) == len(
        right
    ), "left input needs to contain the same number of files as the right input"
    input_str_left = " " + " ".join(left)
    input_str_right = " " + " ".join(right)
    input_cmd = input_str_left + " " + input_str_right
else:
    single = (
        [snakemake.input.single]
        if isinstance(snakemake.input.single, str)
        else snakemake.input.single
    )
    input_cmd = " " + " ".join(single)


outdir = path.dirname(snakemake.output[0])
tmpdir = path.join(outdir, "tmp")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "plass assemble {input_cmd} {snakemake.output} {tmpdir} --threads {snakemake.threads} {snakemake.params.extra} {log}"
)
