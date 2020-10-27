# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for learning error rates on sequence data using dada2 learnErrors function.

# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
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
       extra<-eval(parse(text=snakemake@params[["extra"]]))
       if(is.list(extra)){
           # Add them to the list of arguments
           args<-c(args, extra)
       } else{
           message("Optional R parameters should be passed as a string list")
           message("in the Snakefile. Check the example below:")
           message("params:\n\textra='list(verbose=TRUE, foo=c(1,42) )'")
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

# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
sink(type="message")
sink()
