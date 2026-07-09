__author__ = "Kateřina Havlová"
__copyright__ = "Copyright 2026, Kateřina Havlová"
__email__ = "katkahemalova@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Input: a single BAM/CRAM, or one or more .snf files / a .tsv list (multi-sample).
samples = snakemake.input.get("samples")
samples = " ".join(samples) if isinstance(samples, list) else samples

reference = snakemake.input.get("ref", "")
if reference:
    reference = f"--reference {reference}"

tandem_repeats = snakemake.input.get("tandem_repeats", "")
if tandem_repeats:
    tandem_repeats = f"--tandem-repeats {tandem_repeats}"

genotype_vcf = snakemake.input.get("genotype_vcf", "")
if genotype_vcf:
    genotype_vcf = f"--genotype-vcf {genotype_vcf}"

vcf = snakemake.output.get("vcf", "")
if vcf:
    vcf = f"--vcf {vcf}"

snf = snakemake.output.get("snf", "")
if snf:
    snf = f"--snf {snf}"

if not vcf and not snf:
    raise ValueError("At least one of output.vcf or output.snf must be specified.")


shell(
    "sniffles"
    " --input {samples}"
    " {vcf}"
    " {snf}"
    " {reference}"
    " {tandem_repeats}"
    " {genotype_vcf}"
    " --threads {snakemake.threads}"
    " {extra}"
    " {log}"
)
