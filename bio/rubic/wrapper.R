# __author__ = "Beatrice F. Tan"
# __copyright__ = "Copyright 2018, Beatrice F. Tan"
# __email__ = "beatrice.ftan@gmail.com"
# __license__ = "LUMC"

library(RUBIC)

all_genes <- if (snakemake@params[["genefile"]] == "") system.file("extdata", "genes.tsv", package="RUBIC") else snakemake@params[["genefile"]]
fdr <- if (snakemake@params[["fdr"]] == "") 0.25 else snakemake@params[["fdr"]]

rbc <- rubic(fdr, snakemake@input[["seg"]], snakemake@input[["markers"]], genes=all_genes)
rbc$save.focal.gains(snakemake@output[["out_gains"]])
rbc$save.focal.losses(snakemake@output[["out_losses"]])
rbc$save.plots(snakemake@output[["out_plots"]])
