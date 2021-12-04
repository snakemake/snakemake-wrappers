__author__ = "Tom Poorten"
__copyright__ = "Copyright 2017, Tom Poorten"
__email__ = "tom.poorten@gmail.com"
__license__ = "MIT"

from os import path
from snakemake.shell import shell


inputQuery = " ".join(snakemake.input.query)

# Extract output format
out_name, out_ext = path.splitext(snakemake.output[0])
out_ext = out_ext[1:].upper()

# Extract arguments.
extra = snakemake.params.get("extra", "")

sort = snakemake.params.get("sorting", "none")
sort_extra = snakemake.params.get("sort_extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

pipe_cmd = ""
if out_ext != "PAF":
    # Add option for SAM output
    extra += " -a"

    # Determine which pipe command to use for converting to bam or sorting.
    if sort == "none":

        if out_ext != "SAM":
            # Simply convert to output format using samtools view.
            pipe_cmd = "| samtools view -h --output-fmt {} -".format(out_ext)

    elif sort in ["coordinate", "queryname"]:

        # Add name flag if needed.
        if sort == "queryname":
            sort_extra += " -n"

        # Sort alignments.
        pipe_cmd = "| samtools sort {} --output-fmt {} -".format(sort_extra, out_ext)

    else:
        raise ValueError("Unexpected value for params.sort ({})".format(sort))


shell(
    "(minimap2 -t {snakemake.threads} {extra} "
    "{snakemake.input.target} {inputQuery} {pipe_cmd} > {snakemake.output[0]}) {log}"
)
