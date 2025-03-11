"""Snakemake wrapper for jackhmmer"""

__author__ = "Thomas Mulvaney, N. Tessa Pierce"
__copyright__ = "Copyright 2025, Thomas Mulvaney, N. Tessa Pierce"
__email__ = "mulvaney@mailbox.org"
__license__ = "MIT"

from os import path
from snakemake.shell import shell


# Some parameters are mutually exclusive
def exclusive_parameters(params):
    num_set = 0
    for p in params:
        if snakemake.params.get(p) is not None:
            num_set += 1
        if num_set > 1:
            raise Exception(
                f"Only one of the parameters {', '.join(params)} can be set at a time"
            )


# Map outputs to flags
output_parameters = [
    ("-o", "outfile", ""),
    ("--tblout", "tblout", ""),
    ("--domtblout", "domtblout", ""),
    ("-A", "alignment_hits", ""),
]

# Map parameters to flags
parameters = [
    ("--F1", "filter1"),
    ("--F2", "filter2"),
    ("--F3", "filter3"),
    ("-E", "evalue_threshold"),
    ("-T", "tvalue_threshold"),
    ("--incE", "inclusion_evalue"),
    ("--incT", "inclusion_tvalue"),
]

# Raise an error if any of these are set at the same time
exclusive_parameters(["evalue_threshold", "tvalue_threshold"])
exclusive_parameters(["inclusion_evalue", "inclusion_tvalue"])

out_cmd = ""
for flag, snake_param_name, default in output_parameters:
    out_cmd += f" {flag} {snakemake.output.get(snake_param_name, default)}"


param_cmd = ""
for flag, snake_param_name in parameters:
    value = snakemake.params.get(snake_param_name)
    if value is not None:
        param_cmd += f" {flag} {value}"

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    " jackhmmer --cpu {snakemake.threads} "
    " {out_cmd} {param_cmd} "
    " {snakemake.input.query_file} {snakemake.input.database_file} {log}"
)
