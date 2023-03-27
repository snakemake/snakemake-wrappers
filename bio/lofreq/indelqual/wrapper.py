__author__ = "Tobin Groth"
__copyright__ = "Copyright 2023, Tobin Groth"
__email__ = "tobingroth1@gmail.com"
__license__ = "MIT"


import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
if len(snakemake.output) != 1:
    raise ValueError("Expecting only one output file!")

shell(
    "lofreq indelqual "
    " {bam_input}"
    " -o {output_file}"
    " {extra}"
    " {log}"
)
