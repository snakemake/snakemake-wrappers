# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for plotting the quality profile of reads using dada2 plotQualityProfile function.

# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

library(dada2)

# Plot the quality profile for a given FASTQ file or a list of files
pquality<-plotQualityProfile(unlist(snakemake@input))

# Write the plots to files
library(ggplot2)
ggsave(snakemake@output[[1]], pquality, width = 4, height = 3, dpi = 300)

# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
sink(type="message")
sink()
