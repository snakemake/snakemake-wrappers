__author__ = "Jan Forster"
__copyright__ = "Copyright 2020, Jan Forster"
__email__ = "jan.forster@uk-essen.de"
__license__ = "MIT"

from snakemake.shell import shell

from pathlib import Path

db_dir = Path(snakemake.output[0]).parent.resolve()
reference = "{}.{}".format(snakemake.params["build"], snakemake.params["release"])

log = snakemake.log_fmt_shell(stdout=False, stderr=True)


shell(" snpEff download" " -dataDir {db_dir}" " {reference}" " {log}")
