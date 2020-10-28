# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for inferring sample composition using dada2 dada function.

# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

library(dada2)

# Prepare arguments (no matter the order)
args<-list(
           derep = readRDS(snakemake@input[["derep"]]),
           err = readRDS(snakemake@input[["model"]]),
           multithread = snakemake@threads
           )
# Check if extra params are passed
if(length(snakemake@params) > 0 ){
       # Keeping only the named elements of the list for do.call()
       extra<-snakemake@params[ names(snakemake@params) != "" ]
       if(is.list(extra)){
           # Add them to the list of arguments
           args<-c(args, extra)
       } else{
           message("Optional R parameters should be passed as named Python arguments")
           message("in the Snakefile. Check the example below:")
           message("params:\n\tverbose=True, foo=[1,42]")
           message("Using default parameters from dada2::dada()")
       }
} else{
    message("No optional parameters. Using default parameters from dada2::dada()")
}

# Learn errors rates for both read types
inferred_composition<-do.call(dada, args)

# Store the inferred sample composition as RDS files
saveRDS(inferred_composition, snakemake@output[[1]],compress = T)

# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
sink(type="message")
sink()
