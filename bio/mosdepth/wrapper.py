__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# mosdepth takes additional threads through its option --threads
# One thread for mosdepth
# Other threads are *additional* decompression threads passed to the '--threads' argument
threads = "" if snakemake.threads <= 1 else "{}".format(snakemake.threads - 1)

shell(
    """
    (mosdepth \
        --threads {threads} \
        --by {snakemake.params.by} \
        {extra} \
        {snakemake.params.prefix} \
        {snakemake.input.bam}) {log}
    """
)
