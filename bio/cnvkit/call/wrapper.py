__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2023, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

vcf = snakemake.input.get("vcf", "")
if vcf:
    vcf = f"-v {vcf}"

purity = snakemake.params.get("purity", "")
if purity:
    purity = f"--purity {purity}"

ploidy = snakemake.params.get("ploidy", "")
if ploidy:
    ploidy = f"--ploidy {ploidy}"

filter = snakemake.params.get("filter", "")
if filter:
    filter = "--filter {filter}"

extra = snakemake.params.get("extra", "")

shell(
    "(cnvkit.py call {snakemake.input.segment} "
    "{vcf} "
    "-o {snakemake.output.segment} "
    "{purity} "
    "{ploidy} "
    "{filter} "
    "{extra}) "
    "{log}"
)
