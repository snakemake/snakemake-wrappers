__author__ = "Hamdiye Uzuner"
__copyright__ = "Copyright 2024, Hamdiye Uzuner"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Optional flag for outputting bcf instead of vcf.
output_bcf = snakemake.params.get("output_bcf", False)
output_bcf_flag = "--output-bcf" if output_bcf else ""

shell(
    "orthanq candidates hla --alleles {snakemake.input.alleles} --genome {snakemake.input.genome} "
    " --xml {snakemake.input.xml} {output_bcf_flag} --output {snakemake.output[0]} {log}"
)
