__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from os import path
from snakemake.shell import shell
from snakemake_wrapper_utils.bcftools import get_bcftools_opts


bcftools_opts = get_bcftools_opts(snakemake, parse_memory=False)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    "bcftools concat {snakemake.params.extra} {bcftools_opts} -o {snakemake.output[0]} "
    "{snakemake.input.calls} "
    "{log}"
)
