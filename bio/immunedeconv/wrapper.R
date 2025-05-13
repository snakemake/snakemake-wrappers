# This script takes a gene expression matrix
# and run ImmuneDeconv to estimate immune cell
# population(s).

# __author__ = "Thibault Dayris"
# __copyright__ = "Copyright 2023, Thibault Dayris"
# __email__ = "thibault.dayris@gustaveroussy.fr"
# __license__ = "MIT"

# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
log_file <- base::file(description = snakemake@log[[1]], open = "wt")
base::sink(file = log_file)
base::sink(file = log_file, type = "message")

# Loading libary
base::library("immunedeconv", character.only = TRUE)
base::message("Library loaded")


# Function used to load matrices depending on their format
load_input_file <- function(path) {
    data_matrix <- NULL
    if (base::endsWith(x = path, suffix = "RDS")) {
        data_matrix <- base::readRDS(file = path)
    } else if (base::endsWith(x = path, suffix = "tsv")) {
        data_matrix <- utils::read.table(
            file = path,
            sep = "\t",
            header = TRUE,
            row.names = TRUE
        )
    } else if (base::endsWith(x = path, suffix = "csv")) {
        data_matrix <- utils::read.table(
            file = path,
            sep = ",",
            header = TRUE,
            row.names = TRUE
        )
    }
    base::return(data_matrix)
}

# Setting-up threading (only xCell uses this)
base::Sys.setenv(
    MAX_CORES = base::as.numeric(x = snakemake@threads)
)

# Loading input file, using its extension
# to detect file format
gene_expression_matrix <-  load_input_file(
    path = base::as.character(x = snakemake@input[["expr"]])
)
base::message("Gene expression loaded")

method <- "deconvolute"
if ("method" %in% base::names(x = snakemake@params)) {
    method <- base::as.character(x = snakemake@params[["method"]])
}

# Handling special case of CIBERSORT
if (base::grepl(pattern = "cibersort", x = method, ignore.case = TRUE)) {
    cibersort_binary <- base::as.character(
        x = snakemake@input[["cibersort_binary"]]
    )
    immunedeconv::set_cibersort_binary(path = cibersort_binary)

    cibersort_mat <- base::as.character(
        x = snakemake@input[["cibersort_mat"]]
    )
    immunedeconv::set_cibersort_mat(path = cibersort_mat)
    base::message("CIBERSORT binary and matrix linked")
}

# Build command line
extra <- "gene_expression = gene_expression_matrix"
if ("extra" %in% base::names(x = snakemake@params)) {
    param_extra <- base::as.character(x = snakemake@params[["extra"]])
    if (param_extra != "") {
        extra <- base::paste(
            extra,
            param_extra,
            sep = ", "
        )
    }
}

signature_matrix <- NULL
if ("signature" %in% base::names(x = snakemake@input)) {
    signature_matrix <- load_input_file(
        path = base::as.character(x = snakemake@input[["signature"]])
    )
    extra <- base::paste(
        extra,
        "signature_matrix = signature_matrix",
        sep = ", "
    )
    base::message("Custom signatures loaded")
}

cmd <- base::paste0("immunedeconv::", method, "(", extra, ")")
base::message("Command line used:")
base::message(cmd)

# Running ImmuneDeconv
deconvolution_results <- base::eval(base::parse(text = cmd))
base::message("Immunedeconv done")

# Saving results
output_file <- base::as.character(x = snakemake@output[[1]])
if (base::endsWith(x = output_file, suffix = "RDS")) {
    base::message("Saving results as RDS")
    base::saveRDS(
        object = deconvolution_results,
        file = output_file
    )
} else if (base::endsWith(x = output_file, suffix = "csv")) {
    base::message("Saving results as CSV")
    utils::write.table(
        x = deconvolution_results,
        file = output_file,
        sep = ","
    )
} else if (base::endsWith(x = output_file, suffix = "tsv")) {
    base::message("Saving results as TSV")
    utils::write.table(
        x = deconvolution_results,
        file = output_file,
        sep = "\t"
    )
}
base::message("Process over.")


# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
base::sink(type = "message")
base::sink()