__author__ = "Wibowo Arindrarto"
__copyright__ = "Copyright 2016, Wibowo Arindrarto"
__email__ = "bow@bow.web.id"
__license__ = "BSD"


import os
from pathlib import Path
from snakemake.shell import shell

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")
# Run log
log = snakemake.log_fmt_shell()

# Input file wrangling
reads = snakemake.input.get("reads")
if isinstance(reads, str):
    input_flags = "-U {0}".format(reads)
elif len(reads) == 1:
    input_flags = "-U {0}".format(reads[0])
elif len(reads) == 2:
    input_flags = "-1 {0} -2 {1}".format(*reads)
else:
    raise RuntimeError(
        "Reads parameter must contain at least 1 and at most 2" " input files."
    )

ht2_files = Path(snakemake.input.idx).glob("*.ht2")
idx_prefix = os.path.commonprefix(list(ht2_files)).rstrip(".")

# Executed shell command
shell(
    "(hisat2 {extra} "
    "--threads {snakemake.threads} "
    " -x {idx_prefix} {input_flags} "
    " | samtools view -Sbh -o {snakemake.output[0]} -) "
    " {log}"
)
