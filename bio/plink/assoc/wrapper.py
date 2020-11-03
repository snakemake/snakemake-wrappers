"""Snakemake wrapper for plink"""

__author__ = "Adrián E. Salatino"
__copyright__ = "Copyright 2020, Adrián E. Salatino"
__email__ = "elsalatino@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell


def get_prefix_4(pathList):
    basenames = [x[:-4] for x in pathList]
    if not all(x == basenames[0] for x in basenames):
        raise Exception(
            "Something went wrong between input basenames. Keep multiext() please."
        )
    return basenames[0]


def get_prefix_str(pathList, ext):
    basenames = [x.split("." + ext)[0] for x in pathList]
    if not all(x == basenames[0] for x in basenames):
        raise Exception(
            "Something went wrong between output basenames. Keep multiext() please!"
        )
    return basenames[0]


log = snakemake.log_fmt_shell(stdout=False, stderr=True)
prefix_in = get_prefix_4(snakemake.input)

prefix_out_ext = "assoc"

# In the 6th column of the FAM file: if there are any numeric phenotype values
# other than {-9, 0, 1, 2}, the phenotype is interpreted as a quantitative
# trait instead of case/control status
# prefix_out_ext = "qassoc"

prefix_out = get_prefix_str(snakemake.output, prefix_out_ext)
extra_assoc = snakemake.params.get("extra_assoc", "")

shell(
    "(plink --assoc {extra_assoc}"
    " --threads {snakemake.threads}"
    " --ped {prefix_in}.ped --map {prefix_in}.map"
    " --out {prefix_out} )"
    " {log}"
)
