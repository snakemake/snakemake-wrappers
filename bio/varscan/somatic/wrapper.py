"""Snakemake wrapper for varscan somatic"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


import os.path as op

from snakemake.shell import shell
from snakemake.utils import makedirs

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")

makedirs(op.dirname(snakemake.output[0]))

try:
    # Case there is a mpileup with both normal and tumor
    in_pileup = snakemake.input["mpileup"]
except KeyError:
    # Case there are two separate pileup files
    in_pileup = (
        " {snakemake.input['normal_pileup']}"
        " {snakemake.input['tumor_pileup']} "
    )

shell(
    "varscan somatic"  # Tool and its subcommand
    " {in_pileup}"     # Path to input file(s)
    " {output.vcf}"    # Path to output vcf
    " {extra}"         # Extra parameters
)
