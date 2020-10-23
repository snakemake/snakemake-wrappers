# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for learning error rates on sequence data using dada2 learnErrors function.

# Sink the stderr and stdout to the snakemake log file
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

library(dada2)

# Prepare arguments (no matter the order)
args<-list(
           fls = snakemake@input,
           multithread=snakemake@threads
           )
# Check if extra params are passed
if(length(snakemake@params) > 0 ){
       if(is.list(snakemake@params[[1]])){
           # Add them to the list of arguments
           args<-c(args,snakemake@params[[1]])
       } else{
           message("Optional R parameters should be passed as Python dictionary")
           message("in the Snakefile. Check the example below:")
           message("\tparams: { 'verbose': True, 'foo': [1,42] }")
           message("Using defaults parameters from dada2::learnErrors()")
       }
} else{
    message("No optional parameters. Using defaults parameters from dada2::learnErrors()")
}

# Learn errors rates for both read types
err<-do.call(learnErrors, args)

# Plot estimated versus observed error rates to validate models
perr<-plotErrors(err, nominalQ = TRUE)

# Save the plots
library(ggplot2)
ggsave(snakemake@output[["plot"]], perr, width = 8, height = 8, dpi = 300)

# Store the estimated errors as RDS files
saveRDS(err, snakemake@output[["model"]],compress = T)

# Close the connection for the log file
sink(type="message")
sink()
