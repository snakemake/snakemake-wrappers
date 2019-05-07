__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell
threads = (
    "" if snakemake.threads <= 1
    else " -@ {} ".format(snakemake.threads - 1)
)

shell("samtools merge {threads} {snakemake.params} "
      "{snakemake.output[0]} {snakemake.input}")
