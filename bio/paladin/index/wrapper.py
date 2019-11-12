"""Snakemake wrapper for Paladin Index."""

__author__ = "N. Tessa Pierce"
__copyright__ = "Copyright 2019, N. Tessa Pierce"
__email__ = "ntpierce@gmail.com"
__license__ = "MIT"


# this wrapper temporarily copies your assembly into the output dir
# so that all the paladin output files end up in the desired spot

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

input_assembly = snakemake.input
annotation = snakemake.input.get("gff", "")
paladin_index = str(snakemake.output)
reference_type = snakemake.params.get("reference_type", "3")
assert int(reference_type) in [1, 2, 3, 4]
ref_type_cmd = "-r" + str(reference_type)

output_base = paladin_index.rsplit(".bwt")[0]

shell("cp {input_assembly} {output_base}")
shell("paladin index {ref_type_cmd} {output_base} {annotation} {extra} {log}")
shell("rm -f {output_base}")
