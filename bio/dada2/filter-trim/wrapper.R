# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for filtering single or paired-end reads using dada2 filterAndTrim function.

# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

library(dada2)

# Prepare arguments (no matter the order)
args<-list(
        fwd = snakemake@input[["fwd"]],
        filt = snakemake@output[["filt"]],
        multithread=snakemake@threads
)
# Test if paired end input is passed
if(!is.null(snakemake@input[["rev"]]) & !is.null(snakemake@output[["filt_rev"]])){
        args<-c(args,
            rev = snakemake@input[["rev"]],
            filt.rev = snakemake@output[["filt_rev"]]
            )
}
# Check if extra params are passed
if(length(snakemake@params) > 0 ){
    # Keeping only the named elements of the list for do.call()
    extra<-snakemake@params[ names(snakemake@params) != "" ]
    # Check if 'compress=' option is passed
    if(!is.null(extra[["compress"]])){
        stop("Remove the `compress=` option from `params`.\n",
            "The `compress` option is implicitly set here from the file extension.")
    } else {
        # Check if output files are given as compressed files
        # ex: in se version, all(TRUE, NULL) gives TRUE
        compressed <- c(
            endsWith(args[["filt"]], '.gz'),
            if(is.null(args[["filt.rev"]])) NULL else {endsWith(args[["filt.rev"]], 'gz')}
        )
        if ( all(compressed) ) {
            extra[["compress"]] <- TRUE
        } else if ( any(compressed) ) {
            stop("Either all or no fastq output should be compressed. Please check `output.filt` and `output.filt_rev` for consistency.")
        } else {
            extra[["compress"]] <- FALSE
        }
    }
    # Add them to the list of arguments
    args<-c(args, extra)
} else {
    message("No optional parameters. Using default parameters from dada2::filterAndTrim()")
}

# Call the function with arguments
filt.stats<-do.call(filterAndTrim, args)

# Write processed reads report
write.table(filt.stats, snakemake@output[["stats"]], sep="\t", quote=F)
# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
sink(type="message")
sink()
