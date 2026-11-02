# This wrapper performs MAgeck flute rra downstream analysis

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

# Loading RRA and dropping NA counts that breaks downstream analysis
base::message("Loading and filtering RRA")
rra_gene_summary <- MAGeCKFlute::ReadRRA(
    gene_summary = snakemake@input[["rra"]]
)
rra_gene_summary <- rra_gene_summary[
    !base::is.na(rra_gene_summary$id),
]

rra_sgrna_summary <- NULL
if ("sgrna" %in% base::names(snakemake@input)) {
    rra_sgrna_summary <- MAGeCKFlute::ReadsgRRA(
        sgRNA_summary = snakemake@input[["sgrna"]]
    )
}

# Running MAGeCK flute
base::message("Building command line")
outdir <- base::as.character(x = snakemake@output[[1]])
base::dir.create(
    outdir,
    showWarnings = FALSE,
    recursive = TRUE
)
flute_rra_extra <- base::list(
    gene_summary = rra_gene_summary,
    sgrna_summary = rra_sgrna_summary,
    outdir = outdir
)
if (base::length(snakemake@params) > 0) {
    extra <- snakemake@params[base::names(snakemake@params) != ""]
    flute_rra_extra <- c(flute_rra_extra, extra)
}

base::message("Running MAGeCK command line:")
base::do.call(MAGeCKFlute::FluteRRA, flute_rra_extra)

utils::sessionInfo()
# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
base::sink(type = "message")
base::sink()
