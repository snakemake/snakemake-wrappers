# __author__ = "Charlie Pauvert"
# __copyright__ = "Copyright 2020, Charlie Pauvert"
# __email__ = "cpauvert@protonmail.com"
# __license__ = "MIT"

# Snakemake wrapper for learning error rates separately on paired-end data using dada2 learnErrors function.

library(dada2, quietly=TRUE)

# Preliminary tests -- check if files are empty
fwd.empty<-sapply(snakemake@input[["fwd"]],function(x) file.size(x) == 0)
rev.empty<-sapply(snakemake@input[["rev"]],function(x) file.size(x) == 0)

# Use tests data from the R package to reduce wrapper data load
if( any(fwd.empty) ){
	message("Some input files are empty. Either it is a toy example or it might worth checking")
	fwd<-system.file("extdata", "sam1F.fastq.gz", package="dada2")
} else {
	fwd<-snakemake@input[["fwd"]]
}
if( any(rev.empty) ){
	message("Some input files are empty. Either it is a toy example or it might worth checking")
	rev<-system.file("extdata", "sam1R.fastq.gz", package="dada2")
} else {
	rev<-snakemake@input[["rev"]]
}
# Learn errors rates for both read types
errF<-learnErrors(fwd, multithread = snakemake@threads)
errR<-learnErrors(rev, multithread = snakemake@threads)

# Plot estimated versus observed error rates to validate models
perrF<-plotErrors(errF, nominalQ = TRUE)
perrR<-plotErrors(errR, nominalQ = TRUE)

# Save the plots
library(ggplot2, quietly=TRUE)
ggsave(snakemake@output[["pfwd"]], perrF, width = 8, height = 8, dpi = 300)
ggsave(snakemake@output[["prev"]], perrR, width = 8, height = 8, dpi = 300)

# Store the estimated errors as RDS files
saveRDS(errF, snakemake@output[["mfwd"]],compress = T)
saveRDS(errR, snakemake@output[["mrev"]],compress = T)
