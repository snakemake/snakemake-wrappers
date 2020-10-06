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
filt.stats<-filterAndTrim(snakemake@input[["fwd"]], 
		 snakemake@output[["filt"]], 
		 snakemake@input[["rev"]], 
		 snakemake@output[["filt_rev"]], 
		 maxEE=snakemake@params[["maxEE"]], 
		 truncLen=snakemake@params[["truncLen"]],
		 minLen=snakemake@params[["minLen"]],
		 multithread=snakemake@threads
		 )

# Write processed reads report
write.table(filt.stats, snakemake@output[["stats"]], sep="\t", quote=F)
# Close the connection for the log file
sink(type="message")
sink()
