__author__ = "Hamdiye Uzuner"
__copyright__ = "Copyright 2024, Hamdiye Uzuner"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "orthanq candidates hla --allele-freq {snakemake.input.allele_freqs} "
    " --alleles {snakemake.input.alleles} --genome {snakemake.input.genome} "
    " --xml {snakemake.input.xml} --output {snakemake.output[0]} {log}"
)
