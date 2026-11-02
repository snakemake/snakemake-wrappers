# This wrapper performs Mageck flute mle downstream analysis

# __author__ = "Thibault Dayris"
# __copyright__ = "Copyright 2026, Thibault Dayris"
# __email__ = "thibault.dayris@gustaveroussy.fr"
# __license__ = "MIT"

# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
log_file <- base::file(description = snakemake@log[[1]], open = "wt")
base::sink(file = log_file)
base::sink(file = log_file, type = "message")

base::library(package = "MAGeCKFlute", character.only = TRUE)

# Running MaGeCK flute
base::message("Building command line")
outdir <- base::as.character(x = snakemake@output[[1]])
base::dir.create(
    outdir,
    showWarnings = FALSE,
    recursive = TRUE
)

# Build command line extra parameters
flute_mle_extra <- base::list(
    gene_summary = snakemake@input[[1]],
    outdir = outdir
)
if (base::length(snakemake@params) > 0) {
    extra <- snakemake@params[base::names(snakemake@params) != ""]
    flute_mle_extra <- c(extra, flute_mle_extra)
}

# Run command line
base::message("Running command line:")
base::do.call(MAGeCKFlute::FluteMLE, flute_mle_extra)

utils::sessionInfo()
# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
base::sink(type = "message")
base::sink()
