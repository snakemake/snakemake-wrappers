__author__ = "Jan Forster, Felix Mölder"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de, felix.moelder@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

compress = "| bgzip" if snakemake.output[0].endswith(".gz") else ""

if all(f.endswith(".gz") for f in snakemake.input):
    cat = "zcat"
elif all(not f.endswith(".gz") for f in snakemake.input):
    cat = "cat"
else:
    raise ValueError("Input files must be all compressed or uncompressed.")

shell(
    "({cat} {snakemake.input} | "
    "sort -k1,1 -k2,2n | "
    "bedtools merge"
    " -i stdin"
    " {extra}"
    " {compress}"
    " > {snakemake.output[0]})"
    " {log}"
)
