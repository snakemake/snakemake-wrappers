__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts


samtools_opts = get_samtools_opts(snakemake, parse_output=False)
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
sort = snakemake.params.get("sorting", "none")
sort_extra = snakemake.params.get("sort_extra", "")


pipe_cmd = ""
# Determine which pipe command to use for converting to bam or sorting.
if sort == "none":
    # Simply convert to output format using samtools view.
    pipe_cmd = f"| samtools view -h {sort_extra} {samtools_opts}"
elif sort in ["coordinate", "queryname"]:
    # Add name flag if needed.
    if sort == "queryname":
        sort_extra += " -n"

    # Sort alignments.
    pipe_cmd = f"| samtools sort {sort_extra} {samtools_opts}"
else:
    raise ValueError(f"Unexpected value for params.sort: {sort}")


shell(
    "(bellerophon"
    " --threads {snakemake.threads}"
    " --forward {snakemake.input.fwd}"
    " --reverse {snakemake.input.rev}"
    " {extra}"
    " --output /dev/stdout"
    " {pipe_cmd}"
    " > {snakemake.output[0]}"
    ") {log}"
)
