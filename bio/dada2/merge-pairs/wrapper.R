# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for merging denoised forward and reverse reads using dada2 mergePairs function.

# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

library(dada2)

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
       # Keeping only the named elements of the list for do.call()
       extra<-snakemake@params[ names(snakemake@params) != "" ]
       # Add them to the list of arguments
       args<-c(args, extra)
} else{
    message("No optional parameters. Using default parameters from dada2::mergePairs()")
}

# Merge pairs
merger<-do.call(mergePairs, args)

# Store the estimated errors as RDS files
saveRDS(merger, snakemake@output[[1]],compress = T)

# Close the connection for the log file
sink(type="message")
sink()
