# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for building a sequence - sample table from denoised samples using dada2 makeSequenceTable function.

# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

library(dada2)

# If names are provided use them
nm<-if(is.null(snakemake@params[["names"]])) NULL else snakemake@params[["names"]]

# From a list of n lists to one named list of n elements 
smps<-setNames(
               object=unlist(snakemake@input),
               nm=nm
               )
# Read the RDS into the list
smps<-lapply(smps, readRDS)

# Prepare arguments (no matter the order)
args<-list( samples = smps)
# Check if extra params are passed (apart from [["names"]])
if(length(snakemake@params) > 1 ){
       # Keeping only the named elements of the list for do.call() (apart from [["names"]])
       extra<-snakemake@params[ names(snakemake@params) != "" & names(snakemake@params) != "names" ]
       # Add them to the list of arguments
       args<-c(args, extra)
} else{
    message("No optional parameters. Using default parameters from dada2::makeSequenceTable()")
}

# Make table
seqTab<-do.call(makeSequenceTable, args)

# Store the table as a RDS file
saveRDS(seqTab, snakemake@output[[1]],compress = T)

# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
sink(type="message")
sink()
