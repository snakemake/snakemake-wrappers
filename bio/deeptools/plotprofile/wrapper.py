__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

out_region = snakemake.output.get("regions")
out_data = snakemake.output.get("data")

optional_output = ""

if out_region:
    optional_output += " --outFileSortedRegions {out_region} ".format(
        out_region=out_region
    )

if out_data:
    optional_output += " --outFileNameData {out_data} ".format(out_data=out_data)

os.system(
    f"(plotProfile "
    f"-m {snakemake.input[0]} "
    f"-o {snakemake.output.plot_img} "
    f"{optional_output} "
    f"{snakemake.params}) {log}"
)
