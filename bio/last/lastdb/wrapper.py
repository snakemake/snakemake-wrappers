__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

import os
from os import path


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

protein_cmd = ""
protein = snakemake.params.get("protein_input", False)

if protein:
    protein_cmd = " -p "

os.system(
    f"lastdb {extra} {protein_cmd} -P {snakemake.threads} {snakemake.input} {log}"
)
