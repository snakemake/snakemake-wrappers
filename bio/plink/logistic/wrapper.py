"""Snakemake wrapper for plink"""

__author__ = "Adrián E. Salatino"
__copyright__ = "Copyright 2020, Adrián E. Salatino"
__email__ = "elsalatino@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell


def get_prefix_str(pathList, ext):
    if len(pathList) == 0:
        prefix = "plink"
    else:
        basenames = [x.split("." + ext)[0] for x in pathList]
        if not all(x == basenames[0] for x in basenames):
            raise Exception(
                "Something went wrong between output basenames. Keep multiext() please!"
            )
        prefix = basenames[0]
    return prefix


log = snakemake.log_fmt_shell(stdout=False, stderr=True)
prefix = get_prefix_str(snakemake.output, "assoc.logistic")
extra_logistic = snakemake.params.get("extra_logistic", "")
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
    "(plink --logistic {extra_logistic}" + covar + " --threads {snakemake.threads}"
    " --ped {prefix}.ped --map {prefix}.map"
    " --out {prefix} )"
    " {log}"
)
