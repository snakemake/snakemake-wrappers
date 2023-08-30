__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2016, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

from os.path import splitext
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

# Prefix that should be used for the database
prefix = snakemake.params.get("prefix", splitext(snakemake.output[0])[0])

shell("bwa index -p {prefix} {extra} {snakemake.input} {log}")
