__author__ = "Luca Celebrano"
__copyright__ = "Copyright 2026, Luca Celebrano"
__email__ = "l.celebrano@studenti.unina.it"
__license__ = "MIT"

import shlex
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

# Support optional batch cohort file input (TSV/CSV)
batch_cmd = ""
if snakemake.input:
    cohort = getattr(snakemake.input, "cohort", snakemake.input[0])
    batch_cmd = f"--batch {shlex.quote(str(cohort))}"

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell("cri-calc" " {batch_cmd}" " {extra}" " > {snakemake.output.report:q}" " {log}")
