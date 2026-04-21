__author__ = "Till Hartmann"
__copyright__ = "Copyright 2025, Till Hartmann"
__email__ = "till.hartmann@bih-charite.de"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# required inputs and outputs
if not snakemake.input.get("annotation"):
    raise ValueError("Input 'annotation' is required but not specified")

if not snakemake.output.get("db"):
    raise ValueError("Output 'db' is required but not specified")

sequences = snakemake.input.get("sequences")
if not sequences:
    raise ValueError("Input 'sequences' is required but not specified")

if get_format(sequences) == "fasta":
    sequences = f"--transcript-sequences {sequences}"
else:
    sequences = f"--seqrepo {sequences}"

# required params
if not snakemake.params.get("assembly"):
    raise ValueError("Parameter 'assembly' is required but not specified")

if not snakemake.params.get("transcript_source"):
    raise ValueError("Parameter 'transcript_source' is required but not specified")


# optional params
assembly_version = snakemake.params.get("assembly_version", "")
if assembly_version:
    assembly_version = f"--assembly-version {assembly_version}"

annotation_version = snakemake.params.get("annotation_version", "")
if annotation_version:
    annotation_version = f"--annotation-version {annotation_version}"

transcript_source_version = snakemake.params.get("transcript_source_version", "")
if transcript_source_version:
    transcript_source_version = (
        f"--transcript-source-version {transcript_source_version}"
    )

shell(
    "mehari db create"
    " --threads {snakemake.threads}"
    " --annotation {snakemake.input.annotation:q}"
    " --assembly {snakemake.params.assembly:q}"
    " --transcript-source {snakemake.params.transcript_source:q}"
    " {sequences}"
    " {assembly_version}"
    " {annotation_version}"
    " {transcript_source_version}"
    " {extra}"
    " --output {snakemake.output.db:q}"
    " {log}"
)
