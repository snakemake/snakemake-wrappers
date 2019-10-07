__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


import os
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

bam_input = snakemake.input[0]

if bam_input is None:
    raise ValueError("Missing bam input file!")
elif not len(snakemake.input) == 1:
    raise ValueError("Only expecting one input file: " + str(snakemake.input) + "!")

output_file = snakemake.output[0]

if output_file is None:
    raise ValueError("Missing output file")
elif not len(snakemake.output) == 1:
    raise ValueError("Only expecting one output file: " + str(output_file) + "!")

in_pipe = ""
if bam_input.endswith(".sam"):
    in_pipe = "cat "
else:
    in_pipe = "samtools view -h "

out_pipe = ""
if not output_file.endswith(".sam"):
    out_pipe = " | samtools view -S -b - "

shell(
    " {in_pipe} {bam_input} | " " umis bamtag -" " {out_pipe} > {output_file}" " {log}"
)
