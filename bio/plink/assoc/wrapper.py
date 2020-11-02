"""Snakemake wrapper for plink"""

__author__ = "Adrián E. Salatino"
__copyright__ = "Copyright 2020, Adrián E. Salatino"
__email__ = "elsalatino@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
import os


def getPlinkName(path):
    return [x[::-1] for x in os.path.splitext(os.path.basename(path)[::-1])][-1][:-1]


log = snakemake.log_fmt_shell(stdout=False, stderr=True)
prefix1 = getPlinkName(snakemake.input[0])
prefix2 = getPlinkName(snakemake.output[0])
extra_assoc = snakemake.params.get("extra_assoc", "")

shell(
    "(plink --assoc {extra_assoc}"
    " --threads {snakemake.threads}"
    " --ped {prefix1}.ped --map {prefix1}.map"
    " --out {prefix2} )"
    " {log}"
)
