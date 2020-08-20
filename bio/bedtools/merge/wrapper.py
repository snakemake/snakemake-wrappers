__author__ = "Jan Forster, Felix Mölder"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de, felix.moelder@uni-due.de"
__license__ = "MIT"

import os

## Extract arguments
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
if len(snakemake.input) > 1:
    if all(f.endswith(".gz") for f in snakemake.input):
        cat = "zcat"
    elif all(not f.endswith(".gz") for f in snakemake.input):
        cat = "cat"
    else:
        raise ValueError("Input files must be all compressed or uncompressed.")
    os.system(
        f"({cat} {snakemake.input} | "
        "sort -k1,1 -k2,2n | "
        "bedtools merge {extra} "
        "-i stdin > {snakemake.output}) "
        " {log}"
    )
else:
    os.system(
        f"( bedtools merge"
        " {extra}"
        " -i {snakemake.input}"
        " > {snakemake.output})"
        " {log}"
    )
