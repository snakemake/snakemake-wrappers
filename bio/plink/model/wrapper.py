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
prefix = get_prefix_str(snakemake.output, "model")
extra_model = snakemake.params.get("extra_model", "")

shell(
    "(plink --model {extra_model}"
    " --threads {snakemake.threads}"
    " --ped {prefix}.ped --map {prefix}.map"
    " --out {prefix} )"
    " {log}"
)
