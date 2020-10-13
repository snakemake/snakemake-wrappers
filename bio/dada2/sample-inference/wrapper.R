# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for inferring sample composition using dada2 dada function.

library(dada2, quietly=TRUE)

# Sink the stderr and stdout to the snakemake log file
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

# Prepare arguments (no matter the order)
args<-list(
           derep = readRDS(snakemake@input[["derep"]]),
           err = readRDS(snakemake@input[["model"]]),
           multithread = snakemake@threads
           )
# Check if extra params are passed
if(length(snakemake@params) > 0 ){
    if(length(snakemake@params[[1]]) > 1){
        # Add them to the list of arguments
        args<-c(args,snakemake@params[[1]])
    }
}

# Learn errors rates for both read types
inferred_composition<-do.call(dada, args)

# Store the inferred sample composition as RDS files
saveRDS(inferred_composition, snakemake@output[[1]],compress = T)

# Close the connection for the log file
sink(type="message")
sink()
