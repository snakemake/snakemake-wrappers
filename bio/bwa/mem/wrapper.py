__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell()

shell(
    "(bwa mem {snakemake.params} -t {snakemake.threads} "
    "{snakemake.input.ref} {snakemake.input.sample} "
    "| samtools view -Sbh -o {snakemake.output[0]} -) {log}")
