__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import os
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


out_basename = os.path.commonpath(snakemake.output)


shell("genomescope2 --input {snakemake.input} {extra} --output {out_basename} {log}")
