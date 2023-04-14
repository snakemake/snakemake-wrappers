# __author__ = "Thibault Dayris"
# __copyright__ = "Copyright 2023, Thibault Dayris"
# __email__ = "thibault.dayris@gustaveroussy.fr"
# __license__ = "MIT"

# This script builds a deseq2 dataset from a range of possible input
# files. It also performs relevel if needed.

# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
log.file<-file(snakemake@log[[1]], open = "wt")
base::sink(log.file)
base::sink(log.file, type = "message")

# Loading libraries (order matters)
base::library(package = "tximport", character.only = TRUE)
base::library(package = "readr", character.only = TRUE)
base::library(package = "jsonlite", character.only = TRUE)
base::library(package = "DESeq2", character.only = TRUE)
base::message("Libraries loaded")

# Load colData since it is always used
colData <- utils::read.table(
    file = snakemake@input[["colData"]],
    header = TRUE,
    row.names = 1,
    sep = "\t",
    stringsAsFactors = FALSE
)

# Cast formula from string to R formula
formula <- base::as.formula(x = snakemake@params[["formula"]])
dds_command <- NULL

# Case user provides a Tximport object
if ("txi" %in% base::names(x = snakemake@input)) {
    # Loading tximport object
    txi <- base::readRDS(file = snakemake@input[["txi"]])

    # Acquiring user-defined optional parameters
    dds_parameters <- "txi = txi, colData = colData, design = formula"
    if ("extra" %in% base::names(snakemake@params)) {
        dds_parameters <- base::paste(
            dds_parameters,
            base::as.character(x = snakemake@params[["extra"]]),
            sep = ", "
        )
    }

    # Building command line
    dds_command <- base::paste0(
        "DESeq2::DESeqDataSetFromTximport(",
        dds_parameters,
        ")"
    )

# Case user provides a RangesSummarizedExperiment object
} else if ("rse" %in% base::names(x = snakemake@input)) {
    # Loading RangedSummarizedExperiment object
    se <- base::readRDS(file = snakemake@input[["rse"]])

    # Acquiring user-defined optional parameters
    dds_parameters <- "se = se, design = formula, ignoreRank = FALSE"
    if ("extra" %in% base::names(snakemake@params)) {
        dds_parameters <- base::paste(
            dds_parameters,
            base::as.character(x = snakemake@params[["extra"]]),
            sep = ", "
        )
    }

    # Building command line
    dds_command <- base::paste0(
        "DESeq2::DESeqDataSet(",
        dds_parameters,
        ")"
    )

# Case user provides HTSeq-Count/Feature-Count input files
} else if ("htseq_dir" %in% base::names(x = snakemake@input)) {
    # Casting path in case it contains numbers
    hts_dir <- base::as.character(x = snakemake@input[["htseq_dir"]])

    # Acquiring user-defined optional parameters
    dds_parameters <- "directory = hts_dir, colData = colData, design = formula"
    if ("extra" %in% base::names(snakemake@params)) {
        dds_parameters <- base::paste(
            dds_parameters,
            base::as.character(x = snakemake@params[["extra"]]),
            sep = ", "
        )
    }

    # Building command line
    dds_command <- base::paste0(
        "DESeq2::DESeqDataSetFromHTSeqCount(",
        dds_parameters,
        ")"
    )

# Case user provides an R count matrix as input
} else if ("matrix" %in% base::names(x = snakemake@input)) {
    # Loading RangedSummarizedExperiment object
    count_matrix <- base::readRDS(file = snakemake@input[["matrix"]])

    # Acquiring user-defined optional parameters
    dds_parameters <- ""
    if ("extra" %in% base::names(snakemake@params)) {
        dds_parameters <- base::paste(
            "countData = count_matrix",
            "colData = colData",
            "design = formula",
            "tidy = TRUE",
            base::as.character(x = snakemake@params[["extra"]]),
            sep = ", "
        )
    }

    # Building command line
    dds_command <- base::paste0(
        "DESeq2::DESeqDataSetFromMatrix(",
        dds_parameters,
        ")"
    )

# Case user provides a TSV count matrix as input
} else if ("counts" %in% base::names(x = snakemake@input)) {
    # Loading count table
    count_matrix <- utils::read.table(
        file = snakemake@input[["counts"]],
        header = TRUE,
        se = "\t",
        row.names = 1,
        stringsAsFactors = FALSE
    )

    # Acquiring user-defined optional parameters
    dds_parameters <- ""
    if ("extra" %in% base::names(snakemake@params)) {
        dds_parameters <- base::paste(
            "countData = count_matrix",
            "colData = colData",
            "design = formula",
            "tidy = TRUE",
            base::as.character(x = snakemake@params[["extra"]]),
            sep = ", "
        )
    }

    # Building command line
    dds_command <- base::paste0(
        "DESeq2::DESeqDataSetFromMatrix(",
        dds_parameters,
        ")"
    )
} else {
    base::stop("Error: No counts provided !")
}


base::message("Command line used to build DESeqDataSet object:")
base::message(dds_command)

dds <- base::eval(base::parse(text = dds_command))

# Dropping unused factors and ensuring level ranks on user demand
is_factor <- "factor" %in% base::names(x = snakemake@params)
is_reference <- "reference_level" %in% base::names(x = snakemake@params)
is_test <- "tested_level" %in% base::names(x = snakemake@params)

if (is_factor && is_reference && is_test) {
    # Casting characters in case of factors/levels being numbers
    factor_name <- base::as.character(
        x = snakemake@params[["factor"]]
    )
    reference_name <- base::as.character(
        x = snakemake@params[["reference_level"]]
    )
    test_name <- base::as.character(
        x = snakemake@params[["tested_level"]]
    )

    # Actual relevel
    levels <- c(reference_name, test_name)
    dds[[factor_name]] <- base::factor(
        ddf[[factor_name]], levels = levels
    )
    dds[[factor_name]] <- stats::relevel(
        dds[[factor_name]], ref = reference_level
    )
    dds[[factor_name]] <- base::droplevels(dds[[factor_name]])
    base::message(
        "Factors have been relevel-ed. Reference level: `",
        reference_name,
        "`, tested level: `",
        test_name,
        "`. Factor of interest: `",
        factor_name,
        "`. Other levels have been filtered out."
    )
}

# Dropping null counts (or below threshold) on user demand
if ("min_count" %in% base::names(x = snakemake@params)) {
    count_filter <- base::as.numeric(x = snakemake@params[["min_count"]])
    base::message(
        "Genes with less than ",
        count_filter,
        " estimated/counted reads are filtered out.")
    keep <- base::rowSums(BiocGenerics::counts(dds)) > count_filter
    dds <- dds[keep, ]
}

# Saving DESeqDataSet object
base::saveRDS(
    object = dds,
    file = base::as.character(x = snakemake@output[[0]])
)
base::message("Process over")

# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
base::sink(type = "message")
base::sink()