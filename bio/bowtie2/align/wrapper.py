__author__ = "Johannes Köster, Jorge Langa"
__copyright__ = "Copyright 2024, Johannes Köster, Jorge Langa"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


import tempfile
from os import path

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts
from snakemake_wrapper_utils.samtools import get_samtools_opts


# helpers
def get_extension(filename: str) -> str:
    """
    Return file format since Bowtie2 reads files that
    could be gzip'ed (extension: .gz) or bzip2'ed (extension: .bz2).
    """
    if filename.endswith((".gz", ".bz2")):
        return filename.split(".")[-2].lower()
    return filename.split(".")[-1].lower()


# input
SAMPLE = snakemake.input.sample
INDEX = snakemake.input.idx
REF = snakemake.input.get("ref", None)
REF_FAI = snakemake.input.get("ref_fai", None)

# output
BAM = str(snakemake.output[0])
METRICS = snakemake.output.get("metrics", None)
UNALIGNED = snakemake.output.get("unaligned", None)
UNPAIRED = snakemake.output.get("unpaired", None)
UNCONCORDANT = snakemake.output.get("unconcordant", None)
CONCORDANT = snakemake.output.get("concordant", None)



# log
LOG = snakemake.log_fmt_shell(stdout=False, stderr=True)

# threads
THREADS = snakemake.threads
sort_threads = snakemake.threads - 1


# params
EXTRA = snakemake.params.get("extra", "")
IS_INTERLEAVED = snakemake.params.get("interleaved", False)
SORT_PROGRAM = snakemake.params.get("sort_program", "none")
SORT_ORDER = snakemake.params.get("sort_order", "coordinate")
SORT_EXTRA = snakemake.params.get("sort_extra", "")
SAMTOOLS_OPTS = get_samtools_opts(
    snakemake, parse_threads=False, param_name="sort_extra"
)
JAVA_OPTS = get_java_opts(snakemake)



# check

# check inputs
if not isinstance(SAMPLE, str) and len(SAMPLE) not in [1, 2]:
    raise ValueError("input must have 1 (single-end) or 2 (paired-end) elements")

REQUIRED_IDX = {".1.bt2", ".2.bt2", ".3.bt2", ".4.bt2", ".rev.1.bt2", ".rev.2.bt2"}

index = path.commonprefix(snakemake.input.idx)[:-1]

if len(index) == 0:
    raise ValueError("Could not determine common prefix of inputs.idx files.")

index_extensions = [idx[len(index) :] for idx in snakemake.input.idx]
missing_idx = REQUIRED_IDX - set(index_extensions)
if len(missing_idx) > 0:
    raise ValueError(
        f"Missing required indices: {missing_idx} declared as input.idx.\n"
        f"Identified reference file is {index} with extensions {index_extensions}"
    )

# check outputs
bam_extension = get_extension(BAM)

# check params
if not isinstance(IS_INTERLEAVED, bool):
    raise ValueError("params.interleaved must be a boolean")

if SORT_ORDER not in {"coordinate", "queryname"}:
    raise ValueError(
        f"Unexpected value for sort_order ({SORT_ORDER})"
        "Valid values are 'coordinate' or 'queryname'"
    )

if SORT_PROGRAM not in {"none", "samtools", "picard"}:
    raise ValueError(
        f"Unexpected value for sort_program ({SORT_PROGRAM})"
        "Valid values are 'none', 'samtools' or 'picard'"
    )


# shell.sample


if bam_extension == "cram" and (REF is None or REF_FAI is None):
    raise ValueError(
        "Reference file and index are required for CRAM output."
        "Please specify them as input.ref and input.ref_fai\n"
        f"input.ref: {REF}\n"
        f"input.ref_fai: {REF_FAI}"
    )


CMD_INPUT = ""
if len(SAMPLE) == 1:
    if get_extension(SAMPLE[0]) in ("bam", "sam"):
        CMD_INPUT = f"-b {SAMPLE}"
    else:
        if IS_INTERLEAVED:
            CMD_INPUT = f"--interleaved {SAMPLE}"
        else:
            CMD_INPUT = f"-U {SAMPLE}"
else:
    CMD_INPUT = f"-1 {SAMPLE[0]} -2 {SAMPLE[1]}"

cmd_extra = EXTRA
if all(get_extension(sample) in ("fastq", "fq") for sample in SAMPLE):
    cmd_extra += " -q "
elif all(get_extension(sample) == "tab5" for sample in SAMPLE):
    cmd_extra += " --tab5 "
elif all(get_extension(sample) == "tab6" for sample in SAMPLE):
    cmd_extra += " --tab6 "
elif all(get_extension(sample) in ("fa", "mfa", "fasta") for sample in SAMPLE):
    cmd_extra += " -f "


# shell.threads
if SORT_PROGRAM != "none" and THREADS <= 1:
    raise ValueError(
        "Not enough threads requested. This wrapper requires at least two threads: "
        "one for bowtie2 and one for samtools/picard."
    )


# shell.sort

# Determine which pipe command to use for converting to bam or sorting.
match SORT_PROGRAM:
    case "none":
        # Correctly assign number of threads according to user request
        if sort_threads >= 1:
            SAMTOOLS_OPTS += f" --threads {sort_threads} "
        if BAM.lower().endswith(("bam", "cram")):
            # Simply convert to bam using samtools view.
            PIPE_CMD = f" | samtools view {SAMTOOLS_OPTS} > {BAM} "
        else:
            # Do not perform any sort nor compression, output raw sam
            PIPE_CMD = " > {BAM} "
    case "samtools":
        # Correctly assign number of threads according to user request
        if sort_threads >= 1:
            SAMTOOLS_OPTS += f" --threads {sort_threads} "
        # Add name flag if needed.
        if SORT_ORDER == "queryname":
            SORT_EXTRA += " -n"
        # Sort alignments using samtools sort.
        if bam_extension == "cram":
            SAMTOOLS_OPTS += f" --reference {REF} "
        PIPE_CMD = " | samtools sort {SAMTOOLS_OPTS} {SORT_EXTRA} -T {TMPDIR} > {BAM}"
    case "picard":
        if bam_extension == "cram":
            PICARD_OPTS = f" REFERENCE_SEQUENCE={REF} "
        PIPE_CMD = (
            " | picard SortSam {JAVA_OPTS} {SORT_EXTRA} "
            "--INPUT /dev/stdin "
            "--TMP_DIR {TMPDIR} "
            "--SORT_ORDER {SORT_ORDER} "
            "--OUTPUT {BAM} "
        )


if METRICS:
    cmd_extra += f" --met-file {METRICS} "
if UNALIGNED:
    cmd_extra += f" --un {UNALIGNED} "
if UNPAIRED:
    cmd_extra += f" --al {UNPAIRED} "
if UNCONCORDANT:
    cmd_extra += f" --un-conc {UNCONCORDANT} "
if CONCORDANT:
    cmd_extra += f" --al-conc {CONCORDANT} "


index = path.commonprefix(snakemake.input.idx).rstrip(".")

with tempfile.TemporaryDirectory() as TMPDIR:
    shell(
        "( bowtie2"
        " --threads {THREADS}"
        " {CMD_INPUT} "
        " -x {index}"
        " {cmd_extra}"
        " " + PIPE_CMD + ") {LOG}"
    )
