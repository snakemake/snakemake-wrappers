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
extra_linear = snakemake.params.get("extra_linear", "")
extra_covar = snakemake.params.get("extra_covar", "")
covar_names = snakemake.params.get("covariables", "")

if len(covar_names) > 0:
    covar = " --covar {prefix}.cov {extra_covar} --covar-name "
    for c in covar_names:
        covar += c + ", "
    covar = covar[:-2] + " "

shell(
    "(plink --linear {extra_linear}" + covar + " --threads {snakemake.threads}"
    " --ped {prefix}.ped --map {prefix}.map"
    " --out {prefix} )"
    " {log}"
)
