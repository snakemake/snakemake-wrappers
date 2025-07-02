__author__ = "Till Hartmann"
__copyright__ = "Copyright 2025, Till Hartmann"
__email__ = "till.hartmann@bih-charite.de"
__license__ = "MIT"

from snakemake.shell import shell
import logging

extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

transcript_db = snakemake.input.get("transcript_db", "")
if transcript_db:
    transcript_db = f"--transcripts {transcript_db}"

clinvar_db = snakemake.input.get("clinvar_db", "")
if clinvar_db:
    clinvar_db = f"--clinvar {clinvar_db}"

frequency_db = snakemake.input.get("frequency_db", "")
if frequency_db:
    frequency_db = f"--frequency {frequency_db}"

if not transcript_db and not clinvar_db and not frequency_db:
    raise ValueError(
        "At least one of inputs 'transcript_db', 'clinvar_db' and 'frequency_db' must be specified"
    )

ref = snakemake.input.get("ref", "")
if ref:
    ref = f"--reference {ref}"
    if not snakemake.input.get("fai"):
        raise ValueError("Reference FASTA index must be specified")
else:
    logging.warning(
        "Without reference fasta, cannot do correct HGVS 3' shifting for genomic coordinates."
    )


shell(
    "(mehari annotate seqvars "
    "--path-input-vcf {snakemake.input.calls:q} "
    "{transcript_db} "
    "{clinvar_db} "
    "{frequency_db} "
    "{ref} "
    "{extra} "
    "--path-output-vcf {snakemake.output.calls:q} "
    ") {log}"
)
