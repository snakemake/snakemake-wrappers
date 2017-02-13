__author__ = "Johannes Köster"
__copyright__ = "Copyright 2017, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell()

shell("freebayes {snakemake.params} -f {snakemake.input.ref} "
      "{snakemake.input.samples} > {snakemake.output[0]} {log}")
