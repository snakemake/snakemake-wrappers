# This wrapper performs Mageck flute rra downstream analysis

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
flute_mle_extra <- base::paste0(
    "gene_summary = snakemake@input[[1]], ",
    "treatname = snakemake@params[['treatname']], ",
    "outdir = outdir"
)
if ("extra" %in% base::names(snakemake@params)) {
    flute_mle_extra <- base::paste(
        flute_mle_extra,
        snakemake@params[["extra"]],
        sep = ", "
    )
}

# Run command line
base::message("MaGeCK command line:")
flute_mle_cmd <- base::paste0("MAGeCKFlute::FluteMLE(", flute_mle_extra, ")")
base::message(flute_mle_cmd)
base::eval(base::parse(text = flute_mle_cmd))

utils::sessionInfo()
# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
base::sink(type = "message")
base::sink()
