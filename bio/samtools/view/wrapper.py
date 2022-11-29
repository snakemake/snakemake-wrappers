__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts

samtools_opts = get_samtools_opts(snakemake)
extra = snakemake.params.get("extra", "")
region = snakemake.params.get("region", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)


shell("samtools view {samtools_opts} {extra} {snakemake.input[0]} {region} {log}")
