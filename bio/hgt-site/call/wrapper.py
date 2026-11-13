__author__ = "Iraaj Gangavaram"
__copyright__ = "Copyright 2026, Iraaj Gangavaram"
__email__ = "98648540+iraajgangavaram@users.noreply.github.com"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
host_taxid = snakemake.params["host_taxid"]
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

classifications = snakemake.input.classifications
if isinstance(classifications, str):
    classifications = [classifications]
classifications = " ".join(classifications)

reference = snakemake.input.get("reference", "")
reference = f"--reference {reference}" if reference else ""

annotation = snakemake.input.get("annotation", "")
annotation = f"--annotation {annotation}" if annotation else ""

bed = snakemake.output.get("bed", "")
bed = f"--bed {bed}" if bed else ""

vcf = snakemake.output.get("vcf", "")
vcf = f"--vcf {vcf}" if vcf else ""

multiqc = snakemake.output.get("multiqc", "")
multiqc = f"--multiqc {multiqc}" if multiqc else ""

shell(
    "hgt-site call"
    " --bam {snakemake.input.alignment}"
    " --classifications {classifications}"
    " --host-taxid {host_taxid}"
    " --threads {snakemake.threads}"
    " {reference} {annotation} {bed} {vcf} {multiqc} {extra}"
    " -o {snakemake.output.tsv}"
    " {log}"
)
