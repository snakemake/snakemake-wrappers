__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2021, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts

bcftools_opts = get_bcftools_opts(snakemake)
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

if len(snakemake.output) > 1:
    raise Exception("Only one output file expected, got: " + str(len(snakemake.output)))

filter = snakemake.params.get("filter", "")
extra = snakemake.params.get("extra", "")

shell(
    "bcftools filter {filter} {snakemake.input[0]} "
    "{bcftools_opts} "
    "-o {snakemake.output[0]} "
    "{log}"
)
