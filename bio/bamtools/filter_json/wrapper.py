__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

region = snakemake.params.get("region")
region_param = ""

if region and region is not None:
    region_param = ' -region "' + region + '"'

os.system(
    f"(bamtools filter"
    f" -in {snakemake.input[0]}"
    f" -out {snakemake.output[0]}"
    + region_param
    + f" -script {snakemake.params.json}) {log}"
)
