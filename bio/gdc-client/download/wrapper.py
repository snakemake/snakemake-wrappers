__author__ = "David Lähnemann"
__copyright__ = "Copyright 2020, David Lähnemann"
__email__ = "david.laehnemann@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell
from pathlib import Path

outdir = Path(snakemake.output[0]).parents[1].resolve()
extra = snakemake.params.get("extra", "")
token = snakemake.params.get("gdc_token", "")
if token != "":
    token = "--token-file {}".format(token)

shell("gdc-client download"
      " {token}"
      " {extra}"
      " -n {snakemake.threads} "
      " --log-file {snakemake.log} "
      " --dir {outdir}"
      " {snakemake.wildcards.UUID}")
