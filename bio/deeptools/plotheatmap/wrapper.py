__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

out_region = snakemake.output.get("regions")
out_matrix = snakemake.output.get("heatmap_matrix")

optional_output = ""

if out_region:
    optional_output += " --outFileSortedRegions {out_region} ".format(
        out_region=out_region
    )

if out_matrix:
    optional_output += " --outFileNameMatrix {out_matrix} ".format(
        out_matrix=out_matrix
    )

shell(
    "(plotHeatmap "
    "-m {snakemake.input[0]} "
    "-o {snakemake.output.heatmap_img} "
    "{optional_output} "
    "{extra}) {log}"
)
