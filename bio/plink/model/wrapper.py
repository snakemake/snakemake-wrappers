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
prefix = getPlinkName(snakemake.output[0])
extra_model = snakemake.params.get("extra_model", "")

shell(
    "(plink --model {extra_model}"
    " --threads {snakemake.threads}"
    " --ped {prefix}.ped --map {prefix}.map"
    " --out {prefix} )"
    " {log}"
)
