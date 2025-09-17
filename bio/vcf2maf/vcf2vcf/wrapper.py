# coding: utf-8

"""This wrapper handles vcf2vcf.pl"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from shlex import quote

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Optional input files
chain = snakemake.input.get("chain")
if chain:
    extra += f" --remap-chain={quote(chain)}"

normal_bam = snakemake.input.get("normal_bam")
if normal_bam:
    extra += f" --normal-bam={quote(normal_bam)}"

tumor_bam = snakemake.input.get("tumor_bam")
if tumor_bam:
    extra += f" --tumor-bam={quote(tumor_bam)}"

shell(
    "vcf2vcf.pl"
    " --input-vcf={snakemake.input.vcf:q}"
    " --ref-fasta={snakemake.input.fasta:q}"
    " {extra}"
    " --output-vcf={snakemake.output:q}"
    " {log}"
)
