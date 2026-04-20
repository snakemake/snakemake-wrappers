__author__ = "Till Hartmann"
__copyright__ = "Copyright 2025, Till Hartmann"
__email__ = "till.hartmann@bih-charite.de"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# required inputs and outputs
annotation = snakemake.input.get("annotation")
if not annotation:
    raise ValueError("Input 'annotation' is required but not specified")

output_db = snakemake.output.get("db")
if not output_db:
    raise ValueError("Output 'db' is required but not specified")

sequences = snakemake.input.get("sequences")
if not sequences:
    raise ValueError("Input 'sequences' is required but not specified")

fasta_extensions = (
    ".fasta",
    ".fa",
    ".fna",
    ".fasta.gz",
    ".fasta.bgz",
    ".fa.gz",
    ".fa.bgz",
    ".fna.gz",
    ".fna.bgz",
)
if get_format(sequences) == "fasta":
    seq_arg = f"--transcript-sequences {sequences}"
else:
    seq_arg = f"--seqrepo {sequences}"

# required params
assembly = snakemake.params.get("assembly")
if not assembly:
    raise ValueError("Parameter 'assembly' is required but not specified")

transcript_source = snakemake.params.get("transcript_source")
if not transcript_source:
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
    "(mehari db create "
    "--annotation {annotation:q} "
    "--assembly {assembly:q} "
    "--transcript-source {transcript_source:q} "
    "{seq_arg} "
    "{assembly_version} "
    "{annotation_version} "
    "{transcript_source_version} "
    "--threads {snakemake.threads} "
    "{extra} "
    "--output {output_db:q} "
    ") {log}"
)
