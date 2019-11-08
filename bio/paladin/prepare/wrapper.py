"""Snakemake wrapper for Paladin Prepare"""

__author__ = "Tessa Pierce"
__copyright__ = "Copyright 2019, Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"


# this wrapper temporarily copies your assembly into the output dir
# so that all the paladin output files end up in the desired spot

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

reference_type = snakemake.params.get(
    "reference_type", "1"
)  # download swissprot as default
assert int(reference_type) in [1, 2]
ref_type_cmd = "-r" + str(reference_type)

shell("paladin prepare {ref_type_cmd} {extra} {log}")
