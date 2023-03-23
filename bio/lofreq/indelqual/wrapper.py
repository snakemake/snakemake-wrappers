__author__ = "Tobin Groth"
__copyright__ = "Copyright 2023, Tobin Groth"
__email__ = "tobingroth1@gmail.com"
__license__ = "MIT"


import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

bam_input = snakemake.input.bam

if bam_input is None:
    raise ValueError("Missing bam input file!")

output_file = snakemake.output[0]

if output_file is None:
    raise ValueError("Missing output file")
elif not len(snakemake.output) == 1:
    raise ValueError("Only expecting one output file: " + str(output_file) + "!")

shell(
    "lofreq indelqual "
    " {bam_input}"
    " -o {output_file}"
    " {extra}"
    " {log}"
)
