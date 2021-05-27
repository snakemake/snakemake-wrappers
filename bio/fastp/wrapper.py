__author__ = "Sebastian Kurscheid"
__copyright__ = "Copyright 2019, Sebastian Kurscheid"
__email__ = "sebastian.kurscheid@anu.edu.au"
__license__ = "MIT"

from snakemake.shell import shell
import re

extra = snakemake.params.get("extra", "")
adapters = snakemake.params.get("adapters", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Assert input
n = len(snakemake.input.sample)
assert (
    n == 1 or n == 2
), "input->sample must have 1 (single-end) or 2 (paired-end) elements."


# Input files
if n == 1:
    reads = "--in1 {}".format(snakemake.input.sample)
else:
    reads = "--in1 {} --in2 {}".format(*snakemake.input.sample)


# Output files
trimmed_paths = snakemake.output.get("trimmed", None)
if trimmed_paths:
    if n == 1:
        trimmed = "--out1 {}".format(snakemake.output.trimmed)
    else:
        trimmed = "--out1 {} --out2 {}".format(*snakemake.output.trimmed)

        # Output unpaired files
        unpaired = snakemake.output.get("unpaired", None)
        if unpaired:
            trimmed += f" --unpaired1 {unpaired} --unpaired2 {unpaired}"
        else:
            unpaired1 = snakemake.output.get("unpaired1", None)
            if unpaired1:
                trimmed += f" --unpaired1 {unpaired1}"
            unpaired2 = snakemake.output.get("unpaired2", None)
            if unpaired2:
                trimmed += f" --unpaired2 {unpaired2}"

        # Output merged PE reads
        merged = snakemake.output.get("merged", None)
        if merged:
            if not re.search(r"--merge\b", extra):
                raise ValueError(
                    "output.merged specified but '--merge' option missing from params.extra"
                )
            trimmed += f" --merged_out {merged}"
else:
    trimmed = ""


# Output failed reads
failed = snakemake.output.get("failed", None)
if failed:
    trimmed += f" --failed_out {failed}"


# Stats
html = "--html {}".format(snakemake.output.html)
json = "--json {}".format(snakemake.output.json)


shell(
    "(fastp --thread {snakemake.threads} "
    "{extra} "
    "{adapters} "
    "{reads} "
    "{trimmed} "
    "{json} "
    "{html} ) {log}"
)
