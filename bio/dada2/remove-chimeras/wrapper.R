# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for removing chimeras sequences from 
# the sequence table data using dada2 removeBimeraDenovo function.
library(dada2, quietly=TRUE)

# Sink the stderr and stdout to the snakemake log file
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

# Prepare arguments (no matter the order)
args<-list(
           unqs = readRDS(snakemake@input[[1]]),
           multithread=snakemake@threads
           )
# Check if extra params are passed
if(length(snakemake@params) > 0 ){
       if(length(snakemake@params[[1]]) > 1){
           # Add them to the list of arguments
           args<-c(args,snakemake@params[[1]])
       }
}

# Remove chimeras
seqTab.nochim<-do.call(removeBimeraDenovo, args)

# Store the estimated errors as RDS files
saveRDS(seqTab.nochim, snakemake@output[[1]],compress = T)

# Close the connection for the log file
sink(type="message")
sink()
