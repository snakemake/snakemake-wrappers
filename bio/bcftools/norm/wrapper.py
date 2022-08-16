__author__ = "Dayne Filer"
__copyright__ = "Copyright 2019, Dayne Filer"
__email__ = "dayne.filer@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts

bcftools_opts = get_bcftools_opts(snakemake, parse_memory=False)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell("bcftools norm {bcftools_opts} {extra} {snakemake.input[0]} {log}")
