__author__ = "Jan Forster, Felix Mölder"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "j.forster@dkfz.de, felix.moelder@uni-due.de"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
extra = snakemake.params.get("extra", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
if len(snakemake.input) > 1:
    cat = "zcat" if snakemake.input[0].endswith(".gz") else "cat"
    shell(
        "({cat} {snakemake.input} | "
        "sort -k1,1 -k2,2n | "
        "bedtools merge {extra} "
        "-i stdin > {snakemake.output}) "
        " {log}"
    )
else:
    shell(
        "( bedtools merge"
        " {extra}"
        " -i {snakemake.input}"
        " > {snakemake.output})"
        " {log}"
    )
