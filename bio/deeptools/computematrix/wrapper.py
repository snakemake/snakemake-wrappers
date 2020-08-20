__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

out_tab = snakemake.output.get("matrix_tab")
out_bed = snakemake.output.get("matrix_bed")

optional_output = ""

if out_tab:
    optional_output += " --outFileNameMatrix {out_tab} ".format(out_tab=out_tab)

if out_bed:
    optional_output += " --outFileSortedRegions {out_bed} ".format(out_bed=out_bed)

os.system(
    f"(computeMatrix "
    f"{snakemake.params.command} "
    f"{snakemake.params.extra} "
    f"-R {snakemake.input.bed} "
    f"-S {snakemake.input.bigwig} "
    f"-o {snakemake.output.matrix_gz} "
    f"{optional_output}) {log}"
)
