__author__ = "Jan Forster"
__copyright__ = "Copyright 2021, Jan Forster"
__email__ = "jan.forster@uk-essen.de"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("rbt csv-report {snakemake.input} {snakemake.output} {extra} {log}")
