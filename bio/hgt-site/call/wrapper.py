__author__ = "Iraaj Gangavaram"
__copyright__ = "Copyright 2026, Iraaj Gangavaram"
__email__ = "98648540+iraajgangavaram@users.noreply.github.com"
__license__ = "MIT"


from shlex import quote

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
host_taxid = snakemake.params["host_taxid"]
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

classifications = snakemake.input.classifications
if isinstance(classifications, str):
    classifications = [classifications]


def option(flag, path):
    """An optional flag with its filename quoted, or nothing."""
    return f"{flag} {quote(path)}" if path else ""


reference = option("--reference", snakemake.input.get("reference", ""))
annotation = option("--annotation", snakemake.input.get("annotation", ""))
bed = option("--bed", snakemake.output.get("bed", ""))
vcf = option("--vcf", snakemake.output.get("vcf", ""))
multiqc = option("--multiqc", snakemake.output.get("multiqc", ""))

shell(
    "hgt-site call"
    " --bam {snakemake.input.alignment:q}"
    " --classifications {classifications:q}"
    " --host-taxid {host_taxid}"
    " --threads {snakemake.threads}"
    " {reference} {annotation} {bed} {vcf} {multiqc} {extra}"
    " -o {snakemake.output.tsv:q}"
    " {log}"
)
