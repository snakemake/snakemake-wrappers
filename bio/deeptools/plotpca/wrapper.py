# coding: utf-8

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2024, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


from snakemake.shell import shell

# Optional parameters
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")


# Get plot file format
fmt = str(snakemake.output["plot"]).split(".")[-1].lower()

# Get optional output matrix
pca_tab = snakemake.output.get("matrix")
if pca_tab:
    extra += f" --outFileNameData {pca_tab} "

shell(
    "plotPCA "
    "--corData {snakemake.input[0]} "
    "--plotFile {snakemake.output.plot} "
    "--plotFileFormat {fmt} "
    "{extra} {log}"
)
