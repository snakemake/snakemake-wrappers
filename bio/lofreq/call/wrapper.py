__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2018, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")
ref = snakemake.params.get("ref", None)

if ref is None:
    raise ValueError("A reference must be provided")

bam_input = snakemake.input.bam
bai_input = snakemake.input.bai

if bam_input is None:
    raise ValueError("Missing bam input file!")

if bai_input is None:
    raise ValueError("Missing bai input file!")

output_file = snakemake.output[0]

if output_file is None:
    raise ValueError("Missing output file")
elif not len(snakemake.output) == 1:
    raise ValueError("Only expecting one output file: " + str(output_file) + "!")

shell(
    "lofreq call-parallel "
    " --pp-threads {snakemake.threads}"
    " -f {ref}"
    " {bam_input}"
    " -o {output_file}"
    " {extra}"
    " {log}"
)
