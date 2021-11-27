__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"


from snakemake.shell import shell

# bcftools takes additional decompression threads through --threads
# Other threads are *additional* threads passed to the '--threads' argument
threads = (
    "" if snakemake.threads <= 1 else " --threads {} ".format(snakemake.threads - 1)
)
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "bcftools stats {threads} {snakemake.params} {snakemake.input} > {snakemake.output} {log}"
)
