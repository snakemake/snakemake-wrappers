__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "bcftools concat {snakemake.params} -o {snakemake.output[0]} "
    "{snakemake.input.calls} 2> {log}"
)
