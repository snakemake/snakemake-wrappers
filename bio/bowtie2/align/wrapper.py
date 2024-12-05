__author__ = "Johannes Köster, Jorge Langa"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import tempfile
from os import path
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts
from snakemake_wrapper_utils.samtools import get_samtools_opts

# All idx required by bowtie2
REQUIRED_IDX = {".1.bt2", ".2.bt2", ".3.bt2", ".4.bt2", ".rev.1.bt2", ".rev.2.bt2"}


# Extract arguments.
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
sort_program = snakemake.params.get("sort_program", "none")
sort_order = snakemake.params.get("sort_order", "coordinate")
sort_extra = snakemake.params.get("sort_extra", "")
samtools_opts = get_samtools_opts(
    snakemake, parse_threads=False, param_name="sort_extra"
)
java_opts = get_java_opts(snakemake)

bowtie2_threads = snakemake.threads
samtools_threads = snakemake.threads - 1


# Extract index from input
# and check that all required indices are declared
index = path.commonprefix(snakemake.input.idx)[:-1]

if len(index) == 0:
    raise ValueError("Could not determine common prefix of inputs.idx files.")

index_extensions = [idx[len(index) :] for idx in snakemake.input.idx]
missing_idx = REQUIRED_IDX - set(index_extensions)
if len(missing_idx) > 0:
    raise ValueError(
        f"Missing required indices: {missing_idx} declarad as input.idx.\n"
        f"Identified reference file is {index} with extensions {index_extensions}"
    )


# Check inputs/arguments.
if not isinstance(snakemake.input.sample, str) and len(snakemake.input.sample) not in {
    1,
    2,
}:
    raise ValueError("input must have 1 (single-end) or 2 (paired-end) elements")

if sort_order not in {"coordinate", "queryname"}:
    raise ValueError(f"Unexpected value for sort_order ({sort_order})")


# Determine which pipe command to use for converting to bam or sorting.
if sort_program == "none":
    # Correctly assign number of threads according to user request
    if samtools_threads >= 1:
        samtools_opts += f" --threads {samtools_threads} "

    if str(snakemake.output[0]).lower().endswith(("bam", "cram")):
        # Simply convert to bam using samtools view.
        pipe_cmd = " | samtools view {samtools_opts} > {snakemake.output[0]}"
    else:
        # Do not perform any sort nor compression, output raw sam
        pipe_cmd = " > {snakemake.output[0]} "


elif sort_program == "samtools":
    # Correctly assign number of threads according to user request
    if samtools_threads >= 1:
        samtools_opts += f" --threads {samtools_threads} "

    # Add name flag if needed.
    if sort_order == "queryname":
        sort_extra += " -n"

    # Sort alignments using samtools sort.
    pipe_cmd = " | samtools sort {samtools_opts} {sort_extra} -T {tmpdir} > {snakemake.output[0]}"

elif sort_program == "picard":
    # Correctly assign number of threads according to user request
    bowtie2_threads = bowtie2_threads - 1
    if bowtie2_threads <= 0:
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
    raise ValueError(f"Unexpected value for params.sort ({sort_program})")


def get_format(path: str) -> str:
    """
    Return file format since Bowtie2 reads files that
    could be gzip'ed (extension: .gz) or bzip2'ed (extension: .bz2).
    """
    if path.endswith((".gz", ".bz2")):
        return path.split(".")[-2].lower()
    return path.split(".")[-1].lower()


n = len(snakemake.input.sample)
assert (
    n == 1 or n == 2
), "input->sample must have 1 (single-end) or 2 (paired-end) elements."


sample = ""
if n == 1:
    if get_format(snakemake.input.sample[0]) in ("bam", "sam"):
        sample = f"-b {snakemake.input.sample}"
    else:
        if snakemake.params.get("interleaved", False):
            sample = f"--interleaved {snakemake.input.sample}"
        else:
            sample = f"-U {snakemake.input.sample}"
else:
    sample = "-1 {} -2 {}".format(*snakemake.input.sample)


if all(get_format(sample) in ("fastq", "fq") for sample in snakemake.input.sample):
    extra += " -q "
elif all(get_format(sample) == "tab5" for sample in snakemake.input.sample):
    extra += " --tab5 "
elif all(get_format(sample) == "tab6" for sample in snakemake.input.sample):
    extra += " --tab6 "
elif all(
    get_format(sample) in ("fa", "mfa", "fasta") for sample in snakemake.input.sample
):
    extra += " -f "


metrics = snakemake.output.get("metrics")
if metrics:
    extra += f" --met-file {metrics} "

unaligned = snakemake.output.get("unaligned")
if unaligned:
    extra += f" --un {unaligned} "

unpaired = snakemake.output.get("unpaired")
if unpaired:
    extra += f" --al {unpaired} "

unconcordant = snakemake.output.get("unconcordant")
if unconcordant:
    extra += f" --un-conc {unconcordant} "

concordant = snakemake.output.get("concordant")
if concordant:
    extra += f" --al-conc {concordant} "


index = path.commonprefix(snakemake.input.idx).rstrip(".")


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "( bowtie2"
        " --threads {bowtie2_threads}"
        " {sample} "
        " -x {index}"
        " {extra}"
        " " + pipe_cmd + ") {log}"
    )
