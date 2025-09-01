# coding: utf-8

"""This snakemake wrapper handles sample sheet conversions"""


__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2025, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from os.path import realpath
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import get_format

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

if get_format(str(snakemake.output)) == "json":
    extra = " --output-format json "

if get_format(str(snakemake.input.sample)) == "json":
    extra = " --input-format json "

schema = snakemake.input.get("schema")
if schema:
    schema = realpath(schema)
    extra += f' --schema \'{{"$ref": "file:{schema}"}}\' '

shell("python -m samshee {extra} {snakemake.input.sample} > {snakemake.output} {log}")
