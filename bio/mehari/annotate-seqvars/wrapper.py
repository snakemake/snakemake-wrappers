__author__ = "Till Hartmann"
__copyright__ = "Copyright 2025, Till Hartmann"
__email__ = "till.hartmann@bih-charite.de"
__license__ = "MIT"

from snakemake.shell import shell
import logging

extra = snakemake.params.get("extra", "")

keep_intergenic = str(snakemake.params.get("keep_intergenic", ""))
if keep_intergenic and bool(keep_intergenic):
    keep_intergenic = "--keep-intergenic"

discard_utr_splice_variants = str(
    snakemake.params.get("discard_utr_splice_variants", "")
)
if discard_utr_splice_variants and bool(discard_utr_splice_variants):
    discard_utr_splice_variants = "--discard-utr-splice-variants"

report_most_severe_consequence_by = snakemake.params.get(
    "report_most_severe_consequence_by", ""
)
if report_most_severe_consequence_by:
    if report_most_severe_consequence_by not in {"transcript", "gene", "allele"}:
        raise ValueError(
            "report_most_severe_consequence_by must be either 'transcript', 'gene' or 'allele'"
        )
    report_most_severe_consequence_by = (
        f"--report-most-severe-consequence-by {report_most_severe_consequence_by}"
    )

pick_transcript = snakemake.params.get("pick_transcript", [])
if not isinstance(pick_transcript, list):
    raise ValueError("pick_transcript must be a list")
if pick_transcript:
    pick_transcript = " ".join(f"--pick-transcript {v}" for v in pick_transcript)

pick_transcript_mode = snakemake.params.get("pick_transcript_mode", "")
if pick_transcript_mode:
    if pick_transcript_mode not in {"first", "all"}:
        raise ValueError("pick_transcript_mode must be either 'first' or 'all'")
    pick_transcript_mode = f"--pick-transcript-mode {pick_transcript_mode}"

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

reference_fasta = snakemake.input.get("reference_fasta", "")
if reference_fasta:
    reference_fasta = "--reference {}".format(reference_fasta)
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
    "{reference_fasta} "
    "{keep_intergenic} "
    "{discard_utr_splice_variants} "
    "{pick_transcript} "
    "{pick_transcript_mode} "
    "{report_most_severe_consequence_by} "
    "{extra} "
    "--path-output-vcf {snakemake.output.calls:q} "
    ") {log}"
)
