# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for merging denoised forward and reverse reads using dada2 mergePairs function.

library(dada2, quietly=TRUE)

# Sink the stderr and stdout to the snakemake log file
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

# Prepare arguments (no matter the order)
args<-list(
           dadaF = snakemake@input[["dadaF"]],
           derepF = snakemake@input[["derepF"]],
           dadaR = snakemake@input[["dadaR"]],
           derepR = snakemake@input[["derepR"]]
           )
# Read RDS from the list
args<-sapply(args,readRDS)

# Check if extra params are passed
if(length(snakemake@params) > 0 ){
       if(length(snakemake@params[[1]]) > 1){
           # Add them to the list of arguments
           args<-c(args,snakemake@params[[1]])
       }
}

# Merge pairs
merger<-do.call(mergePairs, args)

# Store the estimated errors as RDS files
saveRDS(merger, snakemake@output[[1]],compress = T)

# Close the connection for the log file
sink(type="message")
sink()
