__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


bcftools_opts = get_bcftools_opts(
    snakemake, parse_output=False, parse_output_format=False, parse_memory=False
)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


shell(
    "bcftools stats"
    " {bcftools_opts}"
    " {extra}"
    " {snakemake.input[0]}"
    " > {snakemake.output[0]}"
    " {log}"
)
