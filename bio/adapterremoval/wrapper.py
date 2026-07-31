__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2020, Filipe G. Vieira"
__license__ = "MIT"

import re
from pathlib import Path
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import is_arg

extra = snakemake.params.get("extra", "") + " "
adapters = snakemake.params.get("adapters", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Check input files
n = len(snakemake.input.sample)
assert (
    n == 1 or n == 2
), "input->sample must have 1 (single-end) or 2 (paired-end) elements."


# Input files
if n == 1 or is_arg("--interleaved", extra) or is_arg("--interleaved-input", extra):
    reads = f"--in-file1 {snakemake.input.sample}"
else:
    reads = "--in-file1 {} --in-file2 {}".format(*snakemake.input.sample)


# Output files
if n == 1 or is_arg("--interleaved", extra) or is_arg("--interleaved-output", extra):
    trimmed = f"--out-file1 {snakemake.output.fq}"
else:
    trimmed = f"--out-file1 {snakemake.output.fq1} --out-file2 {snakemake.output.fq2}"

    # Output singleton files
    singleton = snakemake.output.get("singleton", None)
    if singleton:
        trimmed += f" --out-singleton {singleton}"

    # Output merged PE reads
    merged = snakemake.output.get("merged", None)
    if merged:
        if not is_arg("--merge", extra):
            raise ValueError(
                "output.merged specified but '--merge' option missing from params.extra"
            )
        trimmed += f" --out-merged {merged}"

    # Reports
    out_json = snakemake.output.get("json", "")
    if out_json:
        out_json = f"--out-json {snakemake.output.json}"

    out_html = snakemake.output.get("html", "")
    if out_html:
        out_html = f"--out-html {snakemake.output.html}"


shell(
    "(AdapterRemoval --threads {snakemake.threads} "
    "{reads} "
    "{adapters} "
    "{extra} "
    "{trimmed} "
    "--out-discarded {snakemake.output.discarded} "
    "{out_json}"
    "{out_html}"
    ") {log}"
)
