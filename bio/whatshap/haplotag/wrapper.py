"""Snakemake wrapper for whatshap haplotag."""

__author__ = "Pavel Dimens"
__copyright__ = "Copyright 2023, Pavel Dimens"
__email__ = "pdimens@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "whatshap haplotag"
    "{extra} "
    "--output-threads={snakemake.threads} "
    "-o {snakemake.output} "
    "--reference {snakemake.input.ref} "
    "{snakemake.input.vcf} "
    "{snakemake.input.aln} "
    "{log}"
)
