__author__ = "Till Hartmann"
__copyright__ = "Copyright 2025, Till Hartmann"
__email__ = "till.hartmann@bih-charite.de"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# required inputs and outputs
annotation = snakemake.input.get("annotation")
if not annotation:
    raise ValueError("Input 'annotation' is required but not specified")

output_db = snakemake.output.get("db")
if not output_db:
    raise ValueError("Output 'db' is required but not specified")

seqrepo = snakemake.input.get("seqrepo", "")
if seqrepo:
    seqrepo = f"--seqrepo {seqrepo}"

transcript_sequences = snakemake.input.get("transcript_sequences", "")
if transcript_sequences:
    transcript_sequences = f"--transcript-sequences {transcript_sequences}"

if not (bool(seqrepo) ^ bool(transcript_sequences)):
    raise ValueError(
        "Either 'seqrepo' or 'transcript_sequences' have to be provided. "
    )

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
    transcript_source_version = f"--transcript-source-version {transcript_source_version}"

shell(
    "(mehari db create "
    "--annotation {annotation:q} "
    "--assembly {assembly:q} "
    "--transcript-source {transcript_source:q} "
    "{seqrepo} "
    "{transcript_sequences} "
    "{assembly_version} "
    "{annotation_version} "
    "{transcript_source_version} "
    "--threads {snakemake.threads} "
    "{extra} "
    "--output {output_db:q} "
    ") {log}"
)