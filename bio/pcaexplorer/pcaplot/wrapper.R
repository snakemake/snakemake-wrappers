# This script takes a deseq2 data transform object, performs
# a PCA, and saves results as a PNG file.

# __author__ = "Thibault Dayris"
# __copyright__ = "Copyright 2023, Thibault Dayris"
# __email__ = "thibault.dayris@gustaveroussy.fr"
# __license__ = "MIT"

# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
log_file <- base::file(description = snakemake@log[[1]], open = "wt")
base::sink(file = log_file)
base::sink(file = log_file, type = "message")

# Loading libraries (order matters)
base::library(package = "DESeq2", character.only = TRUE)
base::library(package = "pcaExplorer", character.only = TRUE)
base::message("Libaries loaded")

# Loading input dataset
dst <- base::readRDS(file = base::as.character(x = snakemake@input[[1]]))
base::message("DESeq transformed data loaded")

# Build command line
extra <- "x = dst"
if ("extra" %in% base::names(x = snakemake@params)) {
    user_extra <- base::as.character(x = snakemake@params[["extra"]])
    if (user_extra != "") {
        extra <- base::paste(
            extra,
            user_extra,
            sep = ", "
        )
    }
}

cmd <- base::paste0("pcaExplorer::pcaplot(", extra, ")")
base::message("Command line used: ")
base::message(cmd)

# Build output graph
width <- 480
if ("width" %in% base::names(snakemake@params)) {
    width <- base::as.numeric(x = snakemake@params[["width"]])
}

height <- 480
if ("width" %in% base::names(snakemake@params)) {
    height <- base::as.numeric(x = snakemake@params[["height"]])
}

grDevices::svg(
    filename = snakemake@output[[1]],
    width = width,
    height = height
)

# Running PCA explorer pcaplot:
base::eval(base::parse(text = cmd))

# Saving results
grDevices::dev.off()

base::message("Process over")

# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
base::sink(type = "message")
base::sink()