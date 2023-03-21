"""Snakemake wrapper for Trinity."""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2018, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
# Previous wrapper reserved 10 Gigabytes by default. This behaviour is
# preserved below:
max_memory = "10G"

# Getting memory in megabytes, if java opts is not filled with -Xmx parameter
# By doing so, backward compatibility is preserved
if "mem_mb" in snakemake.resources.keys():
    # max_memory from trinity expects a value in gigabytes.
    rounded_mb_to_gb = int(snakemake.resources["mem_mb"] / 1024)
    max_memory = "{}G".format(rounded_mb_to_gb)

# Getting memory in gigabytes, for user convenience. Please prefer the use
# of mem_mb over mem_gb as advised in documentation.
elif "mem_gb" in snakemake.resources.keys():
    max_memory = "{}G".format(snakemake.resources["mem_gb"])


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
    elif "fa" in left[0] or "fas" in left[0] or "fasta" in left[0]:
        seqtype = "fa"
    else:  # assertion is redundant - warning or error instead?
        assert (
            seqtype is not None
        ), "cannot infer 'fq' or 'fa' seqtype from input files. Please specify 'fq' or 'fa' in 'seqtype' parameter"


shell(
    "Trinity {input_cmd} --CPU {snakemake.threads} "
    " --max_memory {max_memory} --seqType {seqtype} "
    " --output {snakemake.output.dir} {snakemake.params.extra} "
    " {log}"
)
