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
extra_recode = snakemake.params.get("extra_recode", "")
extra_file = snakemake.params.get("extra_file", "")
miss = snakemake.params.get("missing_code", "-9")
pheno_column = snakemake.params.get("phenotype_column_name", "")
sex_column = snakemake.params.get("sex_column_name", "")
male_code = snakemake.params.get("sex_male_code", "")
female_code = snakemake.params.get("sex_female_code", "")
covariables = snakemake.params.get("covariables", "")

if "tab" in extra_recode:
    raise Exception(
        "Sorry, data files must use space separator."
        "Please avoid using 'tab' extra option at recode."
    )

shell(
    "(plink --vcf {snakemake.input.vcf}"
    " --recode {extra_recode} --out {prefix} \n"
    "plink --file {prefix} {extra_file} --make-just-fam --out {prefix} \n"
    "rm {prefix}.nosex)"
    " {log}"
)

import pandas as pd

csv = pd.read_csv(snakemake.input.csv)
ped = pd.read_table(f"{prefix}.ped", sep=" ", header=None)
fam = pd.read_table(f"{prefix}.fam", sep=" ", header=None)

fam[4] = csv[sex_column].map({male_code: 1, female_code: 2})
fam[5] = csv[pheno_column]
ped[list(range(6))] = fam

fam.to_csv(f"{prefix}.fam", sep=" ", na_rep=miss, header=False, index=False)
ped.to_csv(f"{prefix}.ped", sep=" ", na_rep=miss, header=False, index=False)

if len(covariables) > 0:
    cov_columns = [fam[0], fam[1]]
    for c in covariables:
        cov_columns += [csv[c]]
    cov = pd.concat(cov_columns, ignore_index=True, axis=1)
    cov.to_csv(
        f"{prefix}.cov",
        sep=" ",
        na_rep=miss,
        header=["FID", "IID"] + covariables,
        index=False,
    )
