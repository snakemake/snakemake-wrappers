__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

region = snakemake.params.get("region")
region_param = ""

if region and region is not None:
    region_param = ' -region "' + region + '"'

shell(
    "(bamtools filter"
    " -in {snakemake.input[0]}"
    " -out {snakemake.output[0]}"
    + region_param
    + " -script {snakemake.params.json}) {log}"
)
