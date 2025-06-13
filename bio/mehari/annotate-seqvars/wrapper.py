__author__ = "Till Hartmann"
__copyright__ = "Copyright 2025, Till Hartmann"
__email__ = "till.hartmann@bih-charite.de"
__license__ = "MIT"

from snakemake.shell import shell
import logging

# extra options include:
# --report-most-severe-consequence-by {gene, transcript, allele}
# --pick-transcript {mane-select, mane-plus-clinical, length, ensembl-canonical, ref-seq-select, gencode-primary, basic}
# --pick-transcript-mode {first, all} (default: all)
# --keep-intergenic
# --discard-utr-splice-variants
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

reference_fasta = snakemake.input.get("reference_fasta", "")
if reference_fasta:
    reference_fasta = "--reference {}".format(reference_fasta)
else:
    logging.warning("Without reference fasta, cannot do correct HGVS 3' shifting for genomic coordinates.")


shell(
    "(mehari annotate seqvars "
    "--path-input-vcf '{snakemake.input.calls}' "
    "{transcript_db} "
    "{clinvar_db} "
    "{frequency_db} "
    "{reference_fasta} "
    "{extra} "
    "--path-output-vcf {snakemake.output.calls} "
    ") {log}"
)
