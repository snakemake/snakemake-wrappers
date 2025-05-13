__author__ = "Wibowo Arindrarto"
__copyright__ = "Copyright 2016, Wibowo Arindrarto"
__email__ = "bow@bow.web.id"
__license__ = "BSD"


import os
from snakemake.shell import shell

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")
# Run log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Input file wrangling
reads = snakemake.input.get("reads")
if isinstance(reads, str):
    input_flags = f"-U {reads}"
elif len(reads) == 1:
    input_flags = f"-U {reads[0]}"
elif len(reads) == 2:
    input_flags = f"-1 {reads[0]} -2 {reads[1]}"
else:
    raise RuntimeError(
        "Reads parameter must contain at least 1 and at most 2 input files."
    )

# Index path
idx_prefix = os.path.commonprefix(snakemake.input.idx).rstrip(".")

# Executed shell command
shell(
    "(hisat2"
    " --threads {snakemake.threads}"
    " -x {idx_prefix}"
    " {extra}"
    " {input_flags}"
    " | samtools view -Sbh -o {snakemake.output[0]} -"
    ") {log}"
)
