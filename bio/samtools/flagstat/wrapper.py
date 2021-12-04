__author__ = "Christopher Preusch"
__copyright__ = "Copyright 2017, Christopher Preusch"
__email__ = "cpreusch[at]ust.hk"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell("samtools flagstat {snakemake.input[0]} > {snakemake.output[0]} {log}")
