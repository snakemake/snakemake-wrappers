__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2023, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts


java_opts = get_java_opts(snakemake)
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


assert snakemake.params.mode in ["contig", "extend", "correct", "insert", "discard"]


n = len(snakemake.input.sample)
assert (
    n == 1 or n == 2
), "input->sample must have 1 (single-end) or 2 (paired-end) elements."

if n == 1:
    reads = "in={}".format(snakemake.input.sample)
    out = "out={}".format(snakemake.output.out)
else:
    reads = "in={} in2={}".format(*snakemake.input.sample)
    out = "out={} out2={}".format(*snakemake.output.out)


in_extra = snakemake.input.get("extra", "")
if in_extra:
    reads += f" extra={in_extra}"


discarded = snakemake.output.get("discarded", "")
if discarded:
    out += f" outd={discarded}"


shell(
    "tadpole.sh {java_opts}"
    " threads={snakemake.threads}"
    " mode={snakemake.params.mode}"
    " {reads}"
    " {extra}"
    " {out}"
    " {log}"
)
