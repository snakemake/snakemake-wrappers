__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import os
from snakemake.shell import shell

from typing import List, Union


class TooManyInput(Exception):
    def __init__(self, command, nb, max=1):
        super().__init__(
            "Too many input files provided for "
            f"`xsv {command}`. Maximum: {max}, got {nb}"
        )


class TooFewInput(Exception):
    def __init__(self, command, nb, min=2):
        super().__init__(
            "Not enough input files provided for "
            f"`xsv {command}`. Minimum: {min}, got {nb}"
        )


def get_file_nb(snakemakeIO: Union[str, List[str]]) -> int:
    if isinstance(snakemakeIO, str):
        return 1
    return len(snakemakeIO)


def in_delimiter(input: str = snakemake.input) -> str:
    if get_file_nb(input) == 1:
        if str(input).endswith(".tsv"):
            return " --delimiter $'\t' "
    return ""


def out_delimiter(output: str = snakemake.output) -> str:
    if get_file_nb(output) == 1:
        if str(output).endswith(".tsv"):
            return " --out-delimiter $'\t' "
    return ""


def threading(threads: int = snakemake.threads) -> str:
    return f" --jobs {threads} "


def add_extra(
    extra: str,
    add_in_delimiter: bool = False,
    add_out_delimiter: bool = False,
    add_threading: bool = False,
) -> str:
    if add_in_delimiter:
        extra += in_delimiter()
    if add_out_delimiter:
        extra += out_delimiter()
    if add_threading:
        extra += threading()

    return extra


output_command = f"> {snakemake.output}"
extra = snakemake.params.get("extra", "")
command = snakemake.params["subcommand"]
if command == "cat":
    raise ValueError("Use either `cat rows` or `cat columns`, not `cat` alone.")
elif command in ["cat rows", "cat columns"]:
    extra = add_extra(extra, add_in_delimiter=True)
elif command in ["count"]:
    stdout = False
    extra = add_extra(extra, add_in_delimiter=True)
elif command == "fixlength":
    extra = add_extra(extra, add_in_delimiter=True)
    extra += f" --length {snakemake.params.length} "
elif command == "fmt":
    extra = add_extra(extra, add_in_delimiter=True, add_out_delimiter=True)
elif command == "frequency":
    extra = add_extra(extra, add_in_delimiter=True, add_threading=True)
elif command == "headers":
    extra = add_extra(extra, add_in_delimiter=True)


log = snakemake.log_fmt_shell(stdout=False, stderr=True)
shell("xsv {command} {extra} {snakemake.input.table} {output_command} {log}")
