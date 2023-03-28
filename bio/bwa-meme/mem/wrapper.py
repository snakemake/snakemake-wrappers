__author__ = "Christopher Schröder, Johannes Köster, Julian de Ruiter"
__copyright__ = (
    "Copyright 2020, Christopher Schröder, Johannes Köster and Julian de Ruiter"
)
__email__ = "christopher.schroeder@tu-dortmund.de koester@jimmy.harvard.edu, julianderuiter@gmail.com"
__license__ = "MIT"


from os import path

from snakemake.shell import shell


# Extract arguments.
extra = snakemake.params.get("extra", "")

sort = snakemake.params.get("sort", "none")
sort_order = snakemake.params.get("sort_order", "coordinate")
sort_extra = snakemake.params.get("sort_extra", "")
embed_ref = snakemake.params.get("embed_ref", False)

# Option to set the threads of samtools sort and view to the snakemake limit.
# In theory, bwa and alternate and samtools view starts only when sort is
# finished, so that never more threads are used than the limit. But it can
# not always be guaranteed.
exceed_thread_limit = snakemake.params.get("exceed_thread_limit", False)
dedup = snakemake.params.get("dedup", "none")
dedup_extra = snakemake.params.get("dedup_extra", "")

# Detect output format.
if snakemake.output[0].endswith(".sam"):
    output_format = "cram"
elif snakemake.output[0].endswith(".bam"):
    output_format = "bam"
elif snakemake.output[0].endswith(".cram"):
    output_format = "cram"
else:
    raise ValueError("output file format must be .sam, .bam or .cram")

if embed_ref:
    output_format += ",embed_ref"

if exceed_thread_limit:
    samtools_threads = snakemake.threads
else:
    samtools_threads = 1

reference = snakemake.input.get("reference")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Check inputs/arguments.
if not isinstance(snakemake.input.reads, str) and len(snakemake.input.reads) not in {
    1,
    2,
}:
    raise ValueError("input must have 1 (single-end) or 2 (paired-end) elements")

if sort_order not in {"coordinate", "queryname"}:
    raise ValueError("Unexpected value for sort_order ({})".format(sort_order))

# Determine which pipe command to use for converting to bam or sorting.
if sort == "none":
    # Simply convert to bam using samtools view.
    pipe_cmd = "samtools view -h -O {output_format} -o {snakemake.output[0]} -T {reference} -@ {samtools_threads} -"

elif sort == "samtools":
    pipe_cmd = "samtools sort {sort_extra} -O {output_format} -o {snakemake.output[0]} --reference {reference} -@ {samtools_threads} -"

    # Add name flag if needed.
    if sort_order == "queryname":
        sort_extra += " -n"

    prefix = path.splitext(snakemake.output[0])[0]
    sort_extra += " -T " + prefix + ".tmp"

    # Sort alignments using samtools sort.

elif sort == "picard":
    # Sort alignments using picard SortSam.
    pipe_cmd = (
        "picard SortSam {sort_extra} -I /dev/stdin"
        " -O /dev/stdout -SO {sort_order} | samtools view -h -O {output_format} -o {snakemake.output[0]} -T {reference} -@ {samtools_threads} -"
    )
else:
    raise ValueError("Unexpected value for params.sort ({})".format(sort))


# Determine which pipe command to use for converting to bam or sorting.
if dedup == "none":
    # Do not detect duplicates.
    dedup_cmd = ""

elif dedup == "mark":
    # Mark duplicates using samblaster.
    dedup_cmd = "samblaster -q {dedup_extra} | "

elif dedup == "remove":
    dedup_cmd = "samblaster -q -r {dedup_extra} | "

else:
    raise ValueError("Unexpected value for params.dedup ({})".format(dedup))


shell(
    "(bwa-meme mem -7"
    " -t {snakemake.threads}"
    " {extra}"
    " {reference}"
    " {snakemake.input.reads}"
    " | mbuffer -q -m 2G "
    " | " + dedup_cmd + pipe_cmd + ") {log}"
)
