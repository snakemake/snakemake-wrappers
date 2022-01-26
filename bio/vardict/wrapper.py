"""Snakemake wrapper for VarDict Single sample mode"""

__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2021, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"

from pathlib import Path
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

reference = snakemake.input.reference
regions = snakemake.input.regions
bam = snakemake.input.bam
normal = snakemake.input.get("normal", None)
vcf = snakemake.output.vcf

extra = snakemake.params.get("extra", "")
bed_columns = snakemake.params.get("bed_columns", "-c 1 -S 2 -E 3 -g 4")
af_th = snakemake.params.get("allele_frequency_threshold", "0.01")


if normal is None:
    input_bams = bam
    name = snakemake.params.get("sample_name", Path(bam).stem)
    post_scripts = (
        "teststrandbias.R | var2vcf_valid.pl -A -N '" + name + "' -E -f " + af_th
    )
else:
    input_bams = "'" + bam + "|" + normal + "'"
    name = snakemake.params.get("sample_name", Path(bam).stem + "|" + Path(normal).stem)
    post_scripts = 'testsomatic.R | var2vcf_paired.pl -N "' + name + '" -f ' + af_th


shell(
    "vardict-java -G {reference} "
    "-f {af_th} "
    " {extra} "
    "-th {snakemake.threads} "
    "{bed_columns} "
    "-N '{name}' "
    "-b {input_bams} "
    "{regions} |"
    "{post_scripts} "
    "> {vcf}"
    "{log}"
)
