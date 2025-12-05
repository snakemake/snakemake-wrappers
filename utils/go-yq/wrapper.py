# coding: utf-8

"""Snakemake wrapper for go-yq"""

import re
import shlex
import warnings

from snakemake_wrapper_utils.snakemake import is_arg, get_format
from snakemake.shell import shell


def detect_fmt(files, long_option, short_option, extra) -> str:
    """Try to detect input/output formats"""
    formats = [get_format(f) for f in files]
    accepted_formats = {
        "yml": "yaml",
        "yaml": "yaml",
        "json": "json",
        "properties": "props",
        "csv": "csv",
        "tsv": "tsv",
        "toml": "toml",
        "sh": "shell",
        "lua": "lua",
        "ini": "ini",
        "xml": "xml",
    }

    # Ensure user did not provide any format information
    if not (is_arg(long_option, extra) or is_arg(short_option, extra)):
        # Check unique format in input and output separately
        if len(set(formats)) > 1:
            raise ValueError(
                f"The following files: {files}, should have the same extension. "
                f"Got {set(formats)} instead."
            )

        # Trying to detect output format from file extension
        # since yq defaults to yaml output and writes information
        # in standard output.
        fmt = accepted_formats.get(formats[0])
        if fmt:
            return f" {long_option} {fmt}"

    return ""


# Enhance extra parameters if needed
extra = snakemake.params.get("extra", "")
extra += detect_fmt(snakemake.input, "--input-format", "-p", extra)
extra += detect_fmt(snakemake.output, "--output-format", "-o", extra)

subcommand = snakemake.params.get("subcommand", "")
# yq/jq expression should be quoted
expression = shlex.quote(snakemake.params.get("expression", ""))

# Handle the case use creates a file from command line
infile = snakemake.input
if len(infile) == 0:
    infile = " --null-input "

# Handling file splitting
outfile = snakemake.output
if len(snakemake.output) > 1:
    if not (is_arg("--split-exp", extra) or is_arg("-s", extra)):
        raise ValueError(
            "File splitting is not automatically handled. Please provide "
            "adequate '-s/--split-exp' in 'params.extra'."
        )
    log = snakemake.log_fmt_shell(stdout=True, stderr=True)
    outfile = ""
else:
    log = snakemake.log_fmt_shell(stdout=False, stderr=True)
    outfile = f"> {snakemake.output[0]}"

shell("yq {subcommand} {extra} {expression} {infile} {outfile} {log}")
