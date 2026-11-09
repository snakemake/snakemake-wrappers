__author__ = "Luca Celebrano"
__copyright__ = "Copyright 2026, Luca Celebrano"
__email__ = "l.celebrano@studenti.unina.it"
__license__ = "MIT"

import shlex
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# Support optional batch cohort file input (TSV/CSV)
batch_cmd = ""
if snakemake.input:
    batch_cmd = f"--batch {shlex.quote(str(snakemake.input[0]))}"

shell("cri-calc {batch_cmd} {extra} > {snakemake.output.report:q} {log}")
