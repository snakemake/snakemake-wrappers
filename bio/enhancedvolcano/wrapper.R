# __author__ = "Thibault Dayris"
# __copyright__ = "Copyright 2023, Thibault Dayris"
# __email__ = "thibault.dayris@gustaveroussy.fr"
# __license__ = "MIT"

# This script builds a Volcano plot from a table or
# a RDS object that can be casted into a data.frame

# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
log.file <- base::file(snakemake@log[[1]], open = "wt")
base::sink(log.file)
base::sink(log.file, type = "message")

# Loading Libraries and input data
base::library(package = "EnhancedVolcano", character.only = TRUE)
base::message("Library loaded")

input_path <- base::as.character(x = snakemake@input[[1]])
toptable <- NULL
if (base::endsWith(x = input_path, suffix = ".tsv")) {
    toptable <- utils::read.table(
        file = input_path,
        header = TRUE,
        sep = "\t",
        stringsAsFactors = FALSE,
    )
} else if (base::endsWith(x = input_path, suffix = ".csv")) {
   toptable <- utils::read.table(
        file = input_path,
        header = TRUE,
        sep = ",",
        stringsAsFactors = FALSE,
    )
} else if (base::endsWith(x = input_path, suffix = ".RDS")) {
   toptable <- base::readRDS(file = input_path)
} else {
    base::stop(
        "Input file format unknown. Expected either '.tsv', '.csv', or 'RDS'"
    )
}
base::message("Data loaded")

# Building command line
extra <- "toptable = toptable"
if ("extra" %in% base::names(snakemake@params)) {
    extra <- base::paste(
        extra,
        base::as.character(x = snakemake@params[["extra"]]),
        sep = ","
    )
}

width <- 480
if ("width" %in% base::names(snakemake@params)) {
    width <- base::as.numeric(x = snakemake@params[["width"]])
}
height <- 480
if ("height" %in% base::names(snakemake@params)) {
    height <- base::as.numeric(x = snakemake@params[["height"]])
}

cmd <- base::paste0(
    "EnhancedVolcano::EnhancedVolcano(",
    extra,
    ")"
)
base::message("Command line: ")
base::message(cmd)


# Run EnhancedVolcano
grDevices::png(
    filename = base::as.character(x = snakemake@output[[1]]),
    units = "px",
    width = width,
    height = height
)

base::eval(base::parse(text = cmd))

grDevices::dev.off()
base::message("Process over")

# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
base::sink(type = "message")
base::sink()