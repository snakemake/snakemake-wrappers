# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for plotting the quality profile of reads using dada2 plotQualityProfile function.

library(dada2, quietly=TRUE)

# Plot the quality profile for a given FASTQ file
pquality<-plotQualityProfile(snakemake@input[[1]])

# Write the plots to files
library(ggplot2,quietly=TRUE)
ggsave(snakemake@output[[1]], pquality, width = 4, height = 3, dpi = 300)
