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
    in_reads = f"--in-file1 {snakemake.input.sample}"
else:
    in_reads = "--in-file1 {} --in-file2 {}".format(*snakemake.input.sample)


# Output files
if n == 1 or is_arg("--interleaved", extra) or is_arg("--interleaved-output", extra):
    out_trimmed = f"--out-file1 {snakemake.output.fq}"
else:
    out_trimmed = f"--out-file1 {snakemake.output.fq1} --out-file2 {snakemake.output.fq2}"

    # Output singleton files
    singleton = snakemake.output.get("singleton", None)
    if singleton:
        out_trimmed += f" --out-singleton {singleton}"

    # Output merged PE reads
    merged = snakemake.output.get("merged", None)
    if merged:
        if not is_arg("--merge", extra):
            raise ValueError(
                "output.merged specified but '--merge' option missing from params.extra"
            )
        out_trimmed += f" --out-merged {merged}"

    # Output discarded files
    out_discarded = snakemake.output.get("discarded", "")
    if out_discarded:
        out_discarded += f"--out-discarded {out_discarded}"

    # Reports
    out_json = snakemake.output.get("json", "")
    if out_json:
        out_json = f"--out-json {out_json}"

    out_html = snakemake.output.get("html", "")
    if out_html:
        out_html = f"--out-html {out_html}"


shell(
    "(AdapterRemoval --threads {snakemake.threads}"
    " {in_reads}"
    " {adapters}"
    " {extra}"
    " {out_trimmed}"
    " {out_discarded}"
    " {out_json}"
    " {out_html}"
    ") {log}"
)
