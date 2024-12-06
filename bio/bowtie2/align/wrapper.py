__author__ = "Johannes Köster, Jorge Langa"
__copyright__ = "Copyright 2024, Johannes Köster, Jorge Langa"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import tempfile
from os import path

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts
from snakemake_wrapper_utils.samtools import get_samtools_opts


# input.sample
SAMPLE = snakemake.input.sample

N_SAMPLE = len(SAMPLE)

if not isinstance(SAMPLE, str) and N_SAMPLE not in {1, 2, }:
    raise ValueError("input must have 1 (single-end) or 2 (paired-end) elements")

# input.idx
REQUIRED_IDX = {".1.bt2", ".2.bt2", ".3.bt2", ".4.bt2", ".rev.1.bt2", ".rev.2.bt2"}

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


# input.ref
REF = snakemake.input.get("ref", None)

# input.ref_fai
REF_FAI = snakemake.input.get("ref_fai", None)


# output
BAM = str(snakemake.output[0])
metrics = snakemake.output.get("metrics", None)
unaligned = snakemake.output.get("unaligned", None)
unpaired = snakemake.output.get("unpaired", None)
unconcordant = snakemake.output.get("unconcordant", None)
concordant = snakemake.output.get("concordant", None)


# log
LOG = snakemake.log_fmt_shell(stdout=False, stderr=True)

# threads
bowtie2_threads = snakemake.threads
sort_threads = snakemake.threads - 1




# params
extra = snakemake.params.get("extra", "")
interleaved = snakemake.params.get("interleaved", False)
sort_program = snakemake.params.get("sort_program", "none")
sort_order = snakemake.params.get("sort_order", "coordinate")
sort_extra = snakemake.params.get("sort_extra", "")
samtools_opts = get_samtools_opts(
    snakemake, parse_threads=False, param_name="sort_extra"
)
java_opts = get_java_opts(snakemake)

if not isinstance(interleaved, bool):
    raise ValueError("params.interleaved must be a boolean")

if sort_order not in {"coordinate", "queryname"}:
    raise ValueError(
        f"Unexpected value for sort_order ({sort_order})"
        "Valid values are 'coordinate' or 'queryname'"
    )

if sort_program not in {"none", "samtools", "picard"}:
    raise ValueError(
        f"Unexpected value for sort_program ({sort_program})"
        "Valid values are 'none', 'samtools' or 'picard'"
    )



# shell

# shell.sample
def get_extension(filename: str) -> str:
    """
    Return file format since Bowtie2 reads files that
    could be gzip'ed (extension: .gz) or bzip2'ed (extension: .bz2).
    """
    if filename.endswith((".gz", ".bz2")):
        return filename.split(".")[-2].lower()
    return filename.split(".")[-1].lower()


CMD_INPUT = ""
if N_SAMPLE == 1:
    if get_extension(SAMPLE[0]) in ("bam", "sam"):
        CMD_INPUT = f"-b {SAMPLE}"
    else:
        if interleaved:
            CMD_INPUT = f"--interleaved {SAMPLE}"
        else:
            CMD_INPUT = f"-U {SAMPLE}"
else:
    CMD_INPUT = f"-1 {SAMPLE[0]} -2 {SAMPLE[1]}"


if all(get_extension(sample) in ("fastq", "fq") for sample in SAMPLE):
    extra += " -q "
elif all(get_extension(sample) == "tab5" for sample in SAMPLE):
    extra += " --tab5 "
elif all(get_extension(sample) == "tab6" for sample in SAMPLE):
    extra += " --tab6 "
elif all(
    get_extension(sample) in ("fa", "mfa", "fasta") for sample in SAMPLE
):
    extra += " -f "


# shell.threads
if sort_program != "none" and bowtie2_threads <= 1:
    raise ValueError(
        "Not enough threads requested. This wrapper requires at least two threads: "
        "one for bowtie2 and one for samtools/picard."
    )


# shell.sort

# Determine which pipe command to use for converting to bam or sorting.
match sort_program:
    case "none":
        # Correctly assign number of threads according to user request
        if sort_threads >= 1:
            samtools_opts += f" --threads {sort_threads} "
        if BAM.lower().endswith(("bam", "cram")):
            # Simply convert to bam using samtools view.
            PIPE_CMD = f" | samtools view {samtools_opts} > {BAM} "
        else:
            # Do not perform any sort nor compression, output raw sam
            PIPE_CMD = " > {BAM} "
    case "samtools":
        # Correctly assign number of threads according to user request
        if sort_threads >= 1:
            samtools_opts += f" --threads {sort_threads} "
        # Add name flag if needed.
        if sort_order == "queryname":
            sort_extra += " -n"
        # Sort alignments using samtools sort.
        PIPE_CMD = " | samtools sort {samtools_opts} {sort_extra} -T {tmpdir} > {BAM}"
    case "picard":
        PIPE_CMD = (
            " | picard SortSam {java_opts} {sort_extra} "
            "--INPUT /dev/stdin "
            "--TMP_DIR {tmpdir} "
            "--SORT_ORDER {sort_order} "
            "--OUTPUT {BAM} "
        )


if metrics:
    extra += f" --met-file {metrics} "
if unaligned:
    extra += f" --un {unaligned} "
if unpaired:
    extra += f" --al {unpaired} "
if unconcordant:
    extra += f" --un-conc {unconcordant} "
if concordant:
    extra += f" --al-conc {concordant} "


index = path.commonprefix(snakemake.input.idx).rstrip(".")


with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "( bowtie2"
        " --threads {bowtie2_threads}"
        " {CMD_INPUT} "
        " -x {index}"
        " {extra}"
        " " + PIPE_CMD + ") {LOG}"
    )
