"""Snakemake wrapper for plink"""

__author__ = "Adrián E. Salatino"
__copyright__ = "Copyright 2020, Adrián E. Salatino"
__email__ = "elsalatino@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
import pandas as pd


def get_prefix_4(pathList):
    basenames = [x[:-4] for x in pathList]
    if not all(x == basenames[0] for x in basenames):
        raise Exception(
            "Something went wrong between input basenames. Keep multiext() please."
        )
    return basenames[0]


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
prefix_in = get_prefix_4(snakemake.input)
fam = pd.read_table(f"{prefix_in}.fam", sep=" ", header=None)
if len(set(fam[5]).difference({-9, 0, 1, 2})) > 0:
    prefix_out_ext = "qassoc"
else:
    prefix_out_ext = "assoc"
prefix_out = get_prefix_str(snakemake.output, prefix_out_ext)
extra_assoc = snakemake.params.get("extra_assoc", "")

shell(
    "(plink --assoc {extra_assoc}"
    " --threads {snakemake.threads}"
    " --ped {prefix_in}.ped --map {prefix_in}.map"
    " --out {prefix_out} )"
    " {log}"
)
