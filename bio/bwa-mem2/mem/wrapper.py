__author__ = "Christopher Schröder, Johannes Köster, Julian de Ruiter"
__copyright__ = (
    "Copyright 2020, Christopher Schröder, Johannes Köster and Julian de Ruiter"
)
__email__ = "christopher.schroeder@tu-dortmund.de koester@jimmy.harvard.edu, julianderuiter@gmail.com"
__license__ = "MIT"


import itertools
import tempfile
from os import path
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts
from snakemake_wrapper_utils.samtools import get_samtools_opts

# All idx required by bwa-mem2
REQUIRED_IDX = {".0123", ".amb", ".ann", ".bwt.2bit.64", ".pac"}


# Extract arguments.
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
sort = snakemake.params.get("sort", "none")
sort_order = snakemake.params.get("sort_order", "coordinate")
sort_extra = snakemake.params.get("sort_extra", "")
samtools_opts = get_samtools_opts(
    snakemake, parse_threads=False, param_name="sort_extra"
)
java_opts = get_java_opts(snakemake)

bwa_threads = snakemake.threads
samtools_threads = snakemake.threads - 1


def get_common_prefix(strings: list[str]) -> str:
    """Get the longest common prefix for a list of strings.

    Args:
        strings (list[str]): list of strings
    Return:
        common_prefix (str): longest common prefix
    Examples:
        >>> get_common_prefix(["a.fasta.0123", "a.fasta.bwt.2bit.64"."])
        "a.fasta."
    """

    def all_same(x):
        return all(x[0] == y for y in x)

    char_tuples = zip(*strings)
    prefix_tuples = itertools.takewhile(all_same, char_tuples)
    return "".join(x[0] for x in prefix_tuples)


# Extract index from input
# and check that all required indices are declared
index = get_common_prefix(snakemake.input.idx)[:-1]

if len(index) == 0:
    raise ValueError(
        "Could not determine common prefix of index files.\n"
        "Please make sure that the index files are named correctly."
    )

index_extensions = [idx[len(index) :] for idx in snakemake.input.idx]
missing_idx = REQUIRED_IDX - set(index_extensions)
if len(missing_idx) > 0:
    raise ValueError(
        f"Missing required indices: {missing_idx} declarad as input.idx.\n"
        f"Identified reference file is {index} with extensions {index_extensions}"
    )


# Check inputs/arguments.
if not isinstance(snakemake.input.reads, str) and len(snakemake.input.reads) not in {
    1,
    2,
}:
    raise ValueError("input must have 1 (single-end) or 2 (paired-end) elements")

if sort_order not in {"coordinate", "queryname"}:
    raise ValueError(f"Unexpected value for sort_order ({sort_order})")

# Determine which pipe command to use for converting to bam or sorting.
if sort == "none":
    # Correctly assign number of threads according to user request
    if samtools_threads >= 1:
        samtools_opts += f" --threads {samtools_threads} "

    if str(snakemake.output[0]).lower().endswith(("bam", "cram")):
        # Simply convert to bam using samtools view.
        pipe_cmd = " | samtools view {samtools_opts} > {snakemake.output[0]}"
    else:
        # Do not perform any sort nor compression, output raw sam
        pipe_cmd = " > {snakemake.output[0]} "


elif sort == "samtools":
    # Correctly assign number of threads according to user request
    if samtools_threads >= 1:
        samtools_opts += f" --threads {samtools_threads} "

    # Add name flag if needed.
    if sort_order == "queryname":
        sort_extra += " -n"

    # Sort alignments using samtools sort.
    pipe_cmd = " | samtools sort {samtools_opts} {sort_extra} -T {tmpdir} > {snakemake.output[0]}"

elif sort == "picard":
    # Correctly assign number of threads according to user request
    bwa_threads = bwa_threads - 1
    if bwa_threads <= 0:
        raise ValueError(
            "Not enough threads requested. This wrapper requires exactly one more."
        )

    # Sort alignments using picard SortSam.
    pipe_cmd = (
        " | picard SortSam {java_opts} {sort_extra} "
        "--INPUT /dev/stdin "
        "--TMP_DIR {tmpdir} "
        "--SORT_ORDER {sort_order} "
        "--OUTPUT {snakemake.output[0]}"
    )

else:
    raise ValueError(f"Unexpected value for params.sort ({sort})")

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(bwa-mem2 mem"
        " -t {bwa_threads}"
        " {extra}"
        " {index}"
        " {snakemake.input.reads}"
        " " + pipe_cmd + " ) {log}"
    )
