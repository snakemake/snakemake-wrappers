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
    append=True,
)
extra = snakemake.params.get("extra", "")

with TemporaryDirectory() as tempdir:
    old_path = os.getcwd()
    depth_path = os.path.realpath(snakemake.input.depth)
    os.chdir(tempdir)
    shell(f"sexdeterrmine --Input {depth_path} > out.tsv 2> sexdeterrmine.log")

    log = snakemake.log_fmt_shell(
        stdout=False,
        stderr=True,
        append=True,
    )
    shell("tree -shrf {tempdir} {log}")
    os.chdir(old_path)
    os.replace(f"{tempdir}/sexdeterrmine.log", str(snakemake.log))

    tsv = snakemake.output.get("tsv")
    if tsv:
        shell("mv --verbose {tempdir}/out.tsv {tsv} {log}")

    json = snakemake.output.get("json")
    if json:
        shell("mv --verbose {tempdir}/sexdeterrmine.json {json} {log}")
