# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for dereplicating FASTQ files using dada2 derepFastq function.

library(dada2, quietly=TRUE)

# Sink the stderr and stdout to the snakemake log file
log.file<-file(snakemake@log[[1]],open="wt")
sink(log.file)
sink(log.file,type="message")

# Dereplicate
uniques<-derepFastq(snakemake@input[[1]])

# Store as RDS file
saveRDS(uniques,snakemake@output[[1]])

# Close the connection for the log file
sink(type="message")
sink()

