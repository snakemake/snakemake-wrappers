# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for building a sequence - sample table from denoised samples using dada2 makeSequenceTable function.
library(dada2, quietly=TRUE)

# Sink the stderr and stdout to the snakemake log file
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

# From a list of n lists to one named list of n elements 
smps<-setNames(
               object=unlist(snakemake@input),
               nm=snakemake@params[["names"]]
               )
# Read the RDS into the list
smps<-lapply(smps, readRDS)

# Prepare arguments (no matter the order)
args<-list( samples = smps)

# Make table
seqTab<-do.call(makeSequenceTable, args)

# Store the table as a RDS file
saveRDS(seqTab, snakemake@output[[1]],compress = T)

# Close the connection for the log file
sink(type="message")
sink()
