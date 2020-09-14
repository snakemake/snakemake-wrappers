__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

# Samtools takes additional threads through its option -@
# One thread for samtools merge
# Other threads are *additional* threads passed to the '-@' argument
threads = "" if snakemake.threads <= 1 else " -@ {} ".format(snakemake.threads - 1)

shell("samtools merge {threads} {extra} " "{snakemake.output[0]} {snakemake.input}")
