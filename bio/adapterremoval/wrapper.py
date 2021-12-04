__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2020, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell
from pathlib import Path
import re

extra = snakemake.params.get("extra", "") + " "
adapters = snakemake.params.get("adapters", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Check input files
n = len(snakemake.input.sample)
assert (
    n == 1 or n == 2
), "input->sample must have 1 (single-end) or 2 (paired-end) elements."


# Input files
if n == 1 or "--interleaved " in extra or "--interleaved-input " in extra:
    reads = "--file1 {}".format(snakemake.input.sample)
else:
    reads = "--file1 {} --file2 {}".format(*snakemake.input.sample)


# Gzip or Bzip compressed output?
compress_out = ""
if all(
    [
        Path(value).suffix == ".gz"
        for key, value in snakemake.output.items()
        if key != "settings"
    ]
):
    compress_out = "--gzip"
elif all(
    [
        Path(value).suffix == ".bz2"
        for key, value in snakemake.output.items()
        if key != "settings"
    ]
):
    compress_out = "--bzip2"
else:
    raise ValueError(
        "all output files (except for 'settings') must be compressed the same way"
    )


# Output files
if n == 1 or "--interleaved " in extra or "--interleaved-output " in extra:
    trimmed = f"--output1 {snakemake.output.fq}"
else:
    trimmed = f"--output1 {snakemake.output.fq1} --output2 {snakemake.output.fq2}"

    # Output singleton files
    singleton = snakemake.output.get("singleton", None)
    if singleton:
        trimmed += f" --singleton {singleton}"

    # Output collapsed PE reads
    collapsed = snakemake.output.get("collapsed", None)
    if collapsed:
        if not re.search(r"--collapse\b", extra):
            raise ValueError(
                "output.collapsed specified but '--collapse' option missing from params.extra"
            )
        trimmed += f" --outputcollapsed {collapsed}"

    # Output collapsed and truncated PE reads
    collapsed_trunc = snakemake.output.get("collapsed_trunc", None)
    if collapsed_trunc:
        if not re.search(r"--collapse\b", extra):
            raise ValueError(
                "output.collapsed_trunc specified but '--collapse' option missing from params.extra"
            )
        trimmed += f" --outputcollapsedtruncated {collapsed_trunc}"


shell(
    "(AdapterRemoval --threads {snakemake.threads} "
    "{reads} "
    "{adapters} "
    "{extra} "
    "{compress_out} "
    "{trimmed} "
    "--discarded {snakemake.output.discarded} "
    "--settings {snakemake.output.settings}"
    ") {log}"
)
