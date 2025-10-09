__author__ = "Hamdiye Uzuner"
__copyright__ = "Copyright 2025, Hamdiye Uzuner"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

# Parse inputs
reads = snakemake.input.get("reads")
if reads:
    extra += f" --reads {reads}"

genome = snakemake.input.get("genome")
if genome:
    extra += f" --genome {genome}"

alleles = snakemake.input.get("alleles")
if alleles:
    extra += f" --alleles {alleles}"

xml = snakemake.input.get("xml")
if xml:
    extra += f" --xml {xml}"

lineages = snakemake.input.get("lineages")
if lineages:
    extra += f" --lineages {lineages}"

haplotype_variants = snakemake.input.get("haplotype_variants")
if haplotype_variants:
    extra += f" --haplotype-variants {haplotype_variants}"

haplotype_calls = snakemake.input.get("haplotype_calls")
if haplotype_calls:
    extra += f" --haplotype-calls {haplotype_calls}"

vg_index = snakemake.input.get("vg_index")
if vg_index:
    extra += f" --vg-index {vg_index}"


# Parse params
if command == "call":
    extra += f" --prior {snakemake.params.prior}"


# Finalize with output and log
shell(
    "orthanq {snakemake.params.command} {snakemake.params.subcommand} {extra} --output {snakemake.output[0]} {log}"
)
