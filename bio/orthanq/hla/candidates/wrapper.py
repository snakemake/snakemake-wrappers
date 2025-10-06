__author__ = "Hamdiye Uzuner"
__copyright__ = "Copyright 2024, Hamdiye Uzuner"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import infer_out_format

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

#infer output format
def get_output_flag(file_name):
    output_fmt = infer_out_format(file_name)
    
    if output_fmt == "BCF":
        return "--output-bcf"
    elif output_fmt == "VCF":
        return ""
    else:
        return f"Unexpected output format: {output_fmt}"
    

shell(
    "orthanq candidates hla --alleles {snakemake.input.alleles} --genome {snakemake.input.genome} "
    " --xml {snakemake.input.xml} {output_fmt} --output {snakemake.output[0]} {log}"
)
