# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for plotting the quality profiles of paired-end reads using dada2 plotQualityProfile function.

library(dada2, quietly=TRUE)

# Plot the quality profiles for both forward and reverse reads
pquality<-plotQualityProfile(
                        c(snakemake@input[["fwd"]],
                        snakemake@input[["rev"]]
                        )
                    )

# Write the plots to files
library(ggplot2,quietly=TRUE)
ggsave(snakemake@output[["plot"]], pquality, width = 4, height = 3, dpi = 300)
