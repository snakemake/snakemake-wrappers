# coding: utf-8

"""Snakemake wrapper for ripgrep"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2026, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True, append=True)

pattern_file = snakemake.input.get("pattern")
if pattern_file:
    extra += f" --file='{pattern_file}'"

pattern = snakemake.params.get("pattern")
if pattern:
    extra += f" --regexp='{pattern}'"

if not (pattern or pattern_file):
    raise ValueError("Either a `input.pattern` or `params.pattern` has to be provided")

ignore = snakemake.input.get("ignore")
if ignore:
    extra += f" --ignore-file='{ignore}'"

outfile = snakemake.output[0]
if str(outfile).endswith(".json"):
    extra += " --json"

compression_fmts = (".gz", ".lzma", ".bz2", ".xz", ".lz4", ".zst")
if any(str(i).endswith(compression_fmts) for i in snakemake.input):
    extra += f" --search-zip"

input_target = snakemake.input.get("target", "")


# rg returns status 1 for "no matches", so this currently fails the Snakemake job
# instead of producing a valid empty result file. Below, we handle  status 1 as
# success while preserving real errors (status 2 and above).
shell(
    "rg {extra} --threads {snakemake.threads} "
    "{input_target} > {snakemake.output[0]:q} {log} "
    "|| if [ $? -eq 1 ]; then echo 'No match' {log}; else exit $?; fi "
)
