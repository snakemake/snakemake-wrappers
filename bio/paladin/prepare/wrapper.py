"""Snakemake wrapper for Paladin Prepare"""

__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

reference_type = snakemake.params.get(
    "reference_type", "1"
)  # download swissprot as default
assert int(reference_type) in [1, 2]
ref_type_cmd = "-r" + str(reference_type)

shell("paladin prepare {ref_type_cmd} {extra} {log}")
