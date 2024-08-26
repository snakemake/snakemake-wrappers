# coding: utf-8

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2024, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


from snakemake.shell import shell

# Optional parameters
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

# Get required arguments
cor_method = snakemake.params.get("correlation", "spearman")
what_to_plot = snakemake.params.get("plot", "heatmap")

# Get plot file format
fmt = str(snakemake.output["plot"]).split(".")[-1].lower()

# Get optional output matrix
corr_matrix = snakemake.output.get("counts")
if corr_matrix:
    extra += f" --outFileCorMatrix {corr_matrix} "

shell(
    "plotCorrelation "
    "--corData {snakemake.input[0]} "
    "--corMethod {cor_method} "
    "--whatToPlot {what_to_plot} "
    "--plotFile {snakemake.output.plot} "
    "{extra} {log}"
)
