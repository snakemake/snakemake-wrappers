__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2021, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


bcftools_opts = get_bcftools_opts(
    snakemake, parse_ref=False, parse_samples=False, parse_memory=False
)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
filter = snakemake.params.get("filter", "")


if len(snakemake.output) > 1:
    raise Exception("Only one output file expected, got: " + str(len(snakemake.output)))


shell(
    "bcftools filter"
    " {bcftools_opts}"
    " {filter}"
    " {extra}"
    " {snakemake.input[0]}"
    " {log}"
)
