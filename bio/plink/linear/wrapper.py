"""Snakemake wrapper for plink"""

__author__ = "Adrián E. Salatino"
__copyright__ = "Copyright 2020, Adrián E. Salatino"
__email__ = "elsalatino@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

prefix = snakemake.params.get("output_prefix", "")
extra_linear = snakemake.params.get("extra_linear", "")
extra_covar = snakemake.params.get("extra_covar", "")
covar = snakemake.params.get("covar", "")
covar_names = snakemake.params.get("covariables", "")

if covar:
    covar = " --covar {extra_covar} {prefix}.cov "
    if len(covar_names) > 0:
        covar += " --covar-name "
        for c in covar_names:
            covar += c + ", "
        covar = covar[:-2] + " "

shell(
    "(plink --linear {extra_linear}" + covar + " --threads {snakemake.threads}"
    " --ped {prefix}.ped --map {prefix}.map"
    " --out {prefix} )"
    " {log}"
)
