__author__ = "Tom Poorten"
__copyright__ = "Copyright 2017, Tom Poorten"
__email__ = "tom.poorten@gmail.com"
__license__ = "MIT"


from os import path
from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import infer_out_format
from snakemake_wrapper_utils.samtools import get_samtools_opts


samtools_opts = get_samtools_opts(snakemake, parse_output=False)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
sort = snakemake.params.get("sorting", "none")
sort_extra = snakemake.params.get("sort_extra", "")
gap_opening = snakemake.params.get("gap_opening", "")

out_ext = infer_out_format(snakemake.output[0])

pipe_cmd = ""
if out_ext != "PAF":
    # Add option for SAM output
    extra += " -a"

    # Determine which pipe command to use for converting to bam or sorting.
    if sort == "none":
        if out_ext != "SAM":
            # Simply convert to output format using samtools view.
            pipe_cmd = f"| samtools view -h {samtools_opts}"

    elif sort in ["coordinate", "queryname"]:
        # Add name flag if needed.
        if sort == "queryname":
            sort_extra += " -n"

        # Sort alignments.
        pipe_cmd = f"| samtools sort {sort_extra} {samtools_opts}"

    else:
        raise ValueError(f"Unexpected value for params.sort: {sort}")

# prepend -O to the command only if gap_opening is specified
if gap_opening:
    gap_opening = f"-O {gap_opening}"

shell(
    "(minimap2"
    " -t {snakemake.threads}"
    " {extra} "
    " {gap_opening} "
    " {snakemake.input.target}"
    " {snakemake.input.query}"
    " {pipe_cmd}"
    " > {snakemake.output[0]}"
    ") {log}"
)
