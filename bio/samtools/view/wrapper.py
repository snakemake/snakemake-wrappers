__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import get_samtools_opts

samtools_opts = get_samtools_opts(snakemake)
extra = snakemake.params.get("extra", "")
region = snakemake.params.get("region", "")

region_file = snakemake.input.get("region")
if region_file:
    extra += f"--region-file {region_file}"

# Optionally named input
aln = snakemake.input.get("aln")
if not aln:
    aln = snakemake.input[0]

log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)


shell("samtools view {samtools_opts} {extra} {aln} {region} {log}")
