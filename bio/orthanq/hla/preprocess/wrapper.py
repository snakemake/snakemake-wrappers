__author__ = "Hamdiye Uzuner"
__copyright__ = "Copyright 2024, Hamdiye Uzuner"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "orthanq preprocess hla --genome {snakemake.input.genome} "
    " --haplotype-variants {snakemake.input.haplotype_variants} --reads {snakemake.input.reads} "
    " --vg-index {snakemake.input.vg_index} --output {snakemake.output[0]} {log}"
)
