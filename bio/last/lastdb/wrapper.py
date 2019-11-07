__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2010, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from os import path

from snakemake.shell import shell

extra = snakemake.params.get("extra", "-cR01") # want this option? yes/no
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell("lastdb {extra} -P {snakemake.threads} {snakemake.input} {log}")
