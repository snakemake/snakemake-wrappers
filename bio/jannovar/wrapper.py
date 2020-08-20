__author__ = "Bradford Powell"
__copyright__ = "Copyright 2018, Bradford Powell"
__email__ = "bpow@unc.edu"
__license__ = "BSD"


import os

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

pedigree = snakemake.input.get("pedigree", "")
if pedigree:
    pedigree = '--pedigree-file "%s"' % pedigree

os.system(
    f"jannovar annotate-vcf --database {snakemake.params.database}"
    f" --input-vcf {snakemake.input.vcf} --output-vcf {snakemake.output}"
    f" {pedigree} {extra} {log}"
)
