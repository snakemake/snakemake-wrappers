# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for classifying sequences against 
# a reference database using dada2 assignTaxonomy function.

library(dada2, quietly=TRUE)

# Sink the stderr and stdout to the snakemake log file
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

# Prepare arguments (no matter the order)
args<-list(
           seqs = readRDS(snakemake@input[["seqs"]]),
           refFasta = snakemake@input[["refFasta"]],
           multithread=snakemake@threads
           )
# Check if extra params are passed
if(length(snakemake@params) > 0 ){
       if(length(snakemake@params[[1]]) > 1){
           # Add them to the list of arguments
           args<-c(args,snakemake@params[[1]])
       }
}

# Learn errors rates for both read types
taxa<-do.call(assignTaxonomy, args)

# Store the taxonomic assignments as a RDS file
saveRDS(taxa, snakemake@output[[1]],compress = T)

# Close the connection for the log file
sink(type="message")
sink()
