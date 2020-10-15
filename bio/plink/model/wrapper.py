"""Snakemake wrapper for plink"""

__author__ = "Adrián E. Salatino"
__copyright__ = "Copyright 2020, Adrián E. Salatino"
__email__ = "elsalatino@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

prefix = snakemake.params.get("output_prefix", "")
extra_model = snakemake.params.get("extra_model", "")

shell(
    "(plink --model {extra_model}"
    " --threads {snakemake.threads}"
    " --ped {prefix}.ped --map {prefix}.map"
    " --out {prefix} )"
    " {log}"
)
