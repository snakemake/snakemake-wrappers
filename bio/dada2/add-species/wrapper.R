# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for adding species-level 
# annotation using dada2 assignTaxonomy function.

library(dada2, quietly=TRUE)

# Sink the stderr and stdout to the snakemake log file
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

# Prepare arguments (no matter the order)
args<-list(
           taxtab = readRDS(snakemake@input[["taxtab"]]),
           refFasta = snakemake@input[["refFasta"]]
           )
# Check if extra params are passed
if(length(snakemake@params) > 0 ){
       if(length(snakemake@params[[1]]) > 1){
           # Add them to the list of arguments
           args<-c(args,snakemake@params[[1]])
       }
}

# Learn errors rates for both read types
taxa.sp<-do.call(addSpecies, args)

# Store the taxonomic assignments as a RDS file
saveRDS(taxa.sp, snakemake@output[[1]],compress = T)

# Close the connection for the log file
sink(type="message")
sink()
