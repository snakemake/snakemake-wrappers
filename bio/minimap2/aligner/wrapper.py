__author__ = "Tom Poorten"
__copyright__ = "Copyright 2017, Tom Poorten"
__email__ = "tom.poorten@gmail.com"
__license__ = "MIT"


from os import path
from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import infer_out_format
from snakemake_wrapper_utils.samtools import get_samtools_opts


samtools_opts = get_samtools_opts(
    snakemake, parse_output=False, param_name="sort_extra"
)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
sort = snakemake.params.get("sorting", "none")
sort_extra = snakemake.params.get("sort_extra", "")

if isinstance(snakemake.input.query, list):
    in_ext = infer_out_format(snakemake.input.query[0])
    if in_ext == "BAM" and len(snakemake.input.query) > 1:
        raise ValueError(f"uBAM input mode only supports a single uBAM file")
else:
    in_ext = infer_out_format(snakemake.input.query)

pre_cmd = ""
query = ""
if in_ext == "BAM":
    # convert uBAM to fastq keeping all tags
    pre_cmd = f'samtools fastq -T "*" {snakemake.input.query} |'
    # tell minimap2 to parse tags from fastq header
    extra += " -y"
    query = "-"
else:
    query = snakemake.input.query

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

shell(
    "({pre_cmd}"
    " minimap2"
    " -t {snakemake.threads}"
    " {extra} "
    " {snakemake.input.target}"
    " {query}"
    " {pipe_cmd}"
    " > {snakemake.output[0]}"
    ") {log}"
)
