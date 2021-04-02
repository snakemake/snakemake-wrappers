__author__ = "Tom Poorten"
__copyright__ = "Copyright 2017, Tom Poorten"
__email__ = "tom.poorten@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell


inputQuery = " ".join(snakemake.input.query)

# Extract output format
out_name, out_ext = path.splitext(snakemake.output[0])
out_ext = out_ext[1:].upper()

# Extract arguments.
extra = snakemake.params.get("extra", "")

sort = snakemake.params.get("sort", "none")
sort_order = snakemake.params.get("sort_order", "coordinate")
sort_extra = snakemake.params.get("sort_extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Determine which pipe command to use for converting to bam or sorting.
if sort == "none" and out_ext != "SAM":

    # Simply convert to output format using samtools view.
    pipe_cmd = (
        "| samtools view -h --output-fmt " + out_ext + " -"
    )

elif sort == "samtools":

    # Sort alignments using samtools sort.
    pipe_cmd = "| samtools sort {sort_extra} -"

    # Add name flag if needed.
    if sort_order == "queryname":
        sort_extra += " -n"

    # Use prefix for temp.
    prefix = path.splitext(snakemake.output[0])[0]
    sort_extra += " -T " + prefix + ".tmp"

    # Define output format
    sort_extra += " --output-fmt {}".format(out_ext)

elif sort == "picard":

    # Sort alignments using picard SortSam.
    pipe_cmd = (
        "| picard SortSam {sort_extra} INPUT=/dev/stdin"
        " OUTPUT=/dev/stdout SORT_ORDER={sort_order}"
    )

else:
    raise ValueError("Unexpected value for params.sort ({})".format(sort))


shell(
    "(minimap2 -t {snakemake.threads} {extra} "
    "{snakemake.input.target} {inputQuery} {pipe_cmd} > {snakemake.output[0]}) {log}"
)
