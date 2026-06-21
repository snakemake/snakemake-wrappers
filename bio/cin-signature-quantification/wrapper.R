# __author__ = "Carlo Monschein"
# __copyright__ = "Copyright 2026, Carlo Monschein"
# __email__ = "carlo.monschein@hotmail.de"
# __license__ = "MIT"

if (length(snakemake@log) > 0) {
    log <- file(snakemake@log[[1]], open="wt")
    sink(log)
    sink(log, type="message")
    on.exit({
        sink(type = "message")
        sink()
        close(log)
        }, add = TRUE)
}

library(CINSignatureQuantification)

# Input data is absolute copy number profiles in segment table format, containing 
# multiple samples, without allele or subclonal information. It is perferable to use
# unrounded absolute copy number profiles.
segments_file <- snakemake@input[[1]]
out_file <- snakemake@output[[1]]

cat("Quantifing Signatures...", "\n")
Signatures <- quantifyCNSignatures(segments_file)
Signatures_matrix <- getActivities(Signatures)

Signatures_df <- data.frame(Sample = rownames(Signatures_matrix), 
                            Signatures_matrix, 
                            row.names = NULL, 
                            check.names = FALSE)

cat("Saving signatures in: ", out_file, "\n")
write.table(Signatures_df, file = out_file, sep = "\t", quote = FALSE, row.names = FALSE, col.names = TRUE)
