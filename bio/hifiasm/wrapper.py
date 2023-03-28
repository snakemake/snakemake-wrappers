__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2022, Filipe G. Vieira"
__license__ = "MIT"


import os
from snakemake.shell import shell


log = snakemake.log_fmt_shell()
extra = snakemake.params.get("extra", "")


hic1 = snakemake.input.get("hic1", "")
if hic1:
    if isinstance(hic1, list):
        hic1 = ",".join(hic1)
    hic1 = "--h1 {}".format(hic1)

hic2 = snakemake.input.get("hic2", "")
if hic2:
    if isinstance(hic2, list):
        hic2 = ",".join(hic2)
    hic2 = "--h2 {}".format(hic2)


out_prefix = os.path.commonprefix(snakemake.output).rstrip(".")


shell(
    "hifiasm"
    " -t {snakemake.threads}"
    " {extra}"
    " {hic1} {hic2}"
    " -o {out_prefix}"
    " {snakemake.input.fasta}"
    " {log}"
)
