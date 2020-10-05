# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for plotting the quality profiles of paired-end reads using dada2 plotQualityProfile function.

library(dada2, quietly=TRUE)

# Choose n sample(s) at random
sample_to_check<-sample(seq_len(length(snakemake@input[["fwd"]])),snakemake@params[["n"]])

# Plot the quality profiles for both forward and reverse reads
pqF<-plotQualityProfile(snakemake@input[["fwd"]][sample_to_check])
pqR<-plotQualityProfile(snakemake@input[["rev"]][sample_to_check])

# Write the plots to files
library(ggplot2,quietly=TRUE)
ggsave(snakemake@output[["fwd"]], pqF, width = 8, height = 6, dpi = 300)
ggsave(snakemake@output[["rev"]], pqR, width = 8, height = 6, dpi = 300)
