__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

java_opts = get_java_opts(snakemake)
extra = snakemake.params.get("extra", "")
adapters = snakemake.params.get("adapters", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


n = len(snakemake.input.sample)
assert (
    n == 1 or n == 2
), "input->sample must have 1 (single-end) or 2 (paired-end) elements."

if n == 1:
    reads = "in={}".format(snakemake.input.sample)
    trimmed = "out={}".format(snakemake.output.trimmed)
else:
    reads = "in={} in2={}".format(*snakemake.input.sample)
    trimmed = "out={} out2={}".format(*snakemake.output.trimmed)


singleton = snakemake.output.get("singleton", "")
if singleton:
    singleton = f"outs={singleton}"


discarded = snakemake.output.get("discarded", "")
if discarded:
    discarded = f"outm={discarded}"


stats = snakemake.output.get("stats", "")
if stats:
    stats = f"stats={stats}"


shell(
    "bbduk.sh {java_opts} t={snakemake.threads} "
    "{reads} "
    "{adapters} "
    "{extra} "
    "{trimmed} {singleton} {discarded} "
    "{stats} "
    "{log}"
)
