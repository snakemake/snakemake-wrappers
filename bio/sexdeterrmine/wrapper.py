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
)
extra = snakemake.params.get("extra", "")

with TemporaryDirectory() as tempdir:
    old_path = os.getcwd()
    depth_path = os.path.realpath(snakemake.input.depth)
    os.chdir(tempdir)
    commands = [
        f"cd {tempdir}",
        f"sexdeterrmine --Input {depth_path} {extra} > out.tsv",
        f"cd {old_path}",
    ]

    tsv = snakemake.output.get("tsv")
    if tsv:
        commands.append(f"mv --verbose {tempdir}/out.tsv {old_path}/{tsv}")

    json = snakemake.output.get("json")
    if json:
        commands.append(f"mv --verbose {tempdir}/sexdeterrmine.json {old_path}/{json}")

    commands = " && ".join(commands)
    shell("({commands}) {log}")
