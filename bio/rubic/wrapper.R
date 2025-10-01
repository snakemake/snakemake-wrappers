# __author__ = "Beatrice F. Tan"
# __copyright__ = "Copyright 2018, Beatrice F. Tan"
# __email__ = "beatrice.ftan@gmail.com"
# __license__ = "LUMC"

library(RUBIC)

all_genes <- if ("genefile" %in% snakemake@input) snakemake@input[["genefile"]] else system.file("extdata", "genes.tsv", package="RUBIC")
fdr <- if ("fdr" %in% snakemake@params) snakemake@params[["fdr"]] else 0.25

rbc <- rubic(fdr=fdr, seg.cna=snakemake@input[["seg"]], markers=snakemake@input[["markers"]], genes=all_genes)
rbc$save.focal.gains(snakemake@output[["out_gains"]])
rbc$save.focal.losses(snakemake@output[["out_losses"]])
rbc$save.plots(snakemake@output[["out_plots"]])
