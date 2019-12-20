__author__ = "Sebastian Kurscheid"
__copyright__ = "Copyright 2019, Sebastian Kurscheid"
__email__ = "sebastian.kurscheid@anu.edu.au"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

n = len(snakemake.input.sample)
assert (
    n == 1 or n == 2
), "input->sample must have 1 (single-end) or 2 (paired-end) elements."

if n == 1:
    reads = "--in1 {}".format(snakemake.input.sample)
else:
    reads = "--in1 {} --in2 {}".format(*snakemake.input.sample)

trimmed_paths = snakemake.output.get("trimmed", None)
if trimmed_paths is not None:
    if n == 1:
        trimmed = "--out1 {}".format(snakemake.output.trimmed)
    else:
        trimmed = "--out1 {} --out2 {}".format(*snakemake.output.trimmed)
else:
    trimmed = ""

html = "--html {}".format(snakemake.output.html)
json = "--json {}".format(snakemake.output.json)

shell(
    "(fastp --thread {snakemake.threads} {snakemake.params.extra} "
    "{reads} "
    "{trimmed} "
    "{json} "
    "{html} ) {log}"
)
