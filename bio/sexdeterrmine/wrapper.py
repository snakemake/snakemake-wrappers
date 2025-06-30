# coding: utf-8

"""Snakemake wrapper for Sex.DetERRmine"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2024, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory

import os
import os.path

log = snakemake.log_fmt_shell(
    stdout=False,
    stderr=True,
    append=False,
)
extra = snakemake.params.get("extra", "")

with TemporaryDirectory() as tempdir:
    old_path = os.getcwd()
    depth_path = os.path.realpath(snakemake.input.depth)
    os.chdir(tempdir)
    commands = [
        f"cd {tempdir}",
        f"sexdeterrmine --Input {depth_path} {extra} > out.tsv"
        "cd -"
    ]

    tsv = snakemake.output.get("tsv")
    if tsv:
        commands.append("mv --verbose {tempdir}/out.tsv {tsv} {log}")

    json = snakemake.output.get("json")
    if json:
        commands.append("mv --verbose {tempdir}/sexdeterrmine.json {json} {log}")

    commands = '({" && ".join(commands)}) {log}' 
