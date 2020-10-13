# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for filtering paired-end reads using dada2 filterAndTrim function."

library(dada2, quietly=TRUE)

# Sink the stderr and stdout to the snakemake log file
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

# Prepare arguments (no matter the order)
args<-list(
        fwd = snakemake@input[["fwd"]],
        rev = snakemake@input[["rev"]],
        filt = snakemake@output[["filt"]],
        filt.rev = snakemake@output[["filt_rev"]],
        multithread=snakemake@threads
)

# Check if extra params are passed
if(length(snakemake@params) > 0){
    if(length(snakemake@params[[1]]) > 1){
    # Add them to the list of arguments
       args<-c(args,snakemake@params[[1]])
    }
}

# Call the function with arguments
filt.stats<-do.call(filterAndTrim, args)

# Write processed reads report
write.table(filt.stats, snakemake@output[["stats"]], sep="\t", quote=F)
# Close the connection for the log file
sink(type="message")
sink()
