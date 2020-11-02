"""Snakemake wrapper for Unicycler"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2020, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from os.path import dirname
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)
extra = snakemake.params.get("extra", "")

input_reads = ""
if "paired" in snakemake.input.keys():
    input_reads += " --short1 {} --short2 {}".format(*snakemake.input.paired)
if "unpaired" in snakemake.input.keys():
    input_reads += " --unpaired {} ".format(snakemake.input["unpaired"])
if "long" in snakemake.input.keys():
    input_reads += " --long {} ".format(snakemake.input["long"])

output_dir = " --out {} ".format(dirname(snakemake.output[0]))

shell(
    " unicycler "
    " {input_reads} "
    " --threads {snakemake.threads} "
    " {output_dir} "
    " {extra} "
    " {log} "
)
