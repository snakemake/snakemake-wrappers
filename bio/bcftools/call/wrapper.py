__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


bcftools_opts = get_bcftools_opts(snakemake, parse_ref=False, parse_memory=False)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


class CallerOptionError(Exception):
    pass


valid_caller_opts = {"-c", "--consensus-caller", "-m", "--multiallelic-caller"}

caller_opt = snakemake.params.get("caller", "")
if caller_opt.strip() not in valid_caller_opts:
    raise CallerOptionError(
        "bcftools call expects either -m/--multiallelic-caller or "
        "-c/--consensus-caller as caller option."
    )


shell(
    "bcftools call"
    " {bcftools_opts}"
    " {caller_opt}"
    " {extra}"
    " {snakemake.input[0]}"
    " {log}"
)
