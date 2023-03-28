__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.samtools import infer_out_format


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


if snakemake.input[0].endswith(".gz"):
    pipe = "gunzip -c"
elif snakemake.input[0].endswith(".bz2"):
    pipe = "bunzip2 -c"
elif infer_out_format(snakemake.input[0]) in ["SAM", "BAM", "CRAM"]:
    pipe = "samtools view -h"
else:
    pipe = "cat"


shell(
    "({pipe}"
    " {snakemake.input} | "
    "PretextMap"
    " {extra}"
    " -o {snakemake.output}"
    ") {log}"
)
