"""Snakemake wrapper for samtools fixmate"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import os
import os.path as op

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")

# Samtools' threads parameter lists ADDITIONAL threads.
# that is why threads - 1 has to be given to the -@ parameter
threads = "" if snakemake.threads <= 1 else " -@ {} ".format(snakemake.threads - 1)

# Only create the output directory if it doesn't exist
output_dir = op.dirname(snakemake.output[0])
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

os.system(
    f"samtools fixmate {extra} {threads} {snakemake.input[0]} {snakemake.output[0]}"
)
