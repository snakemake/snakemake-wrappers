__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2020, Filipe G. Vieira"
__license__ = "MIT"

import os.path
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

in_bam = snakemake.input.get("bam", "")
if in_bam:
    in_bam = "--input " + in_bam

output_folder = os.path.dirname(snakemake.output.get("log", ""))
if not output_folder:
    raise ValueError("mapDamage2 rule needs output 'log'.")

rescaled_bam = snakemake.output.get("rescaled_bam", "")
if rescaled_bam:
    rescaled_bam = "--rescale --rescale-out " + rescaled_bam


shell(
    "mapDamage "
    "{in_bam} "
    "--reference {snakemake.input.ref} "
    "--folder {output_folder} "
    "{rescaled_bam} "
    "{extra} "
    "{log}"
)
