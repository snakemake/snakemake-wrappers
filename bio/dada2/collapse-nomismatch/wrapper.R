# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for combining together sequences that are identical
# up to shifts and/or indels using dada2 collapseNoMismatch function

# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

library(dada2)

# Prepare arguments (no matter the order)
args<-list(
           seqtab = readRDS(snakemake@input[[1]])
           )
# Check if extra params are passed
if(length(snakemake@params) > 0 ){
       # Keeping only the named elements of the list for do.call()
       extra<-snakemake@params[ names(snakemake@params) != "" ]
       # Add them to the list of arguments
       args<-c(args, extra)
} else{
    message("No optional parameters. Using default parameters from dada2::collapseNoMismatch()")
}

# Collapse sequences
taxa<-do.call(collapseNoMismatch, args)

# Store the resulting table as a RDS file
saveRDS(taxa, snakemake@output[[1]],compress = T)

# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
sink(type="message")
sink()
