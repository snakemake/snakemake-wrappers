# __author__ = "Thibault Dayris"
# __copyright__ = "Copyright 2023, Thibault Dayris"
# __email__ = "thibault.dayris@gustaveroussy.fr"
# __license__ = "MIT"

# This script builds a deseq2 dataset from a range of possible input
# files. It also performs relevel if needed,
# as well as count filtering.

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


# A small function to add user-defined parameters
# if and only if this parameter is not null **and** not
# empty (R does not like trailing commas on function calls)
add_extra <- function(wrapper_defined) {
    if ("extra" %in% base::names(snakemake@params)) {
        # Then user defined optional parameters
        user_defined <- snakemake@params[["extra"]]

        if ((user_defined != "") && inherits(user_defined, "character")) {
            # Then there paremters are non-empty characters
            base::return(
                base::paste(
                    wrapper_defined,
                    user_defined,
                    sep = ", "
                )
            )
        }
    }

    # Case user did not provide any optional parameter
    # or did provide a non/empty character value
    base::return(wrapper_defined)
}

colData <- NULL
if ("colData" %in% base::names(snakemake@input)) {
    # Load colData
    colData <- utils::read.table(
        file = snakemake@input[["colData"]],
        header = TRUE,
        row.names = 1,
        sep = "\t",
        stringsAsFactors = FALSE
    )
    base::print(head(colData))
}

# Cast formula from string to R formula
formula <- stats::as.formula(object = snakemake@params[["formula"]])
base::print(formula)
dds_command <- NULL

# Case user provides a Tximport/Tximeta object
if ("txi" %in% base::names(x = snakemake@input)) {
    if (base::is.null(colData)) {
        base::stop(
            "When a `txi` dataset is provided in input,",
            " then a `colData` is expected"
        )
    }

    # Loading tximport object
    txi <- base::readRDS(file = snakemake@input[["txi"]])

    # Acquiring user-defined optional parameters
    dds_parameters <- add_extra(
        wrapper_defined = "txi = txi, colData = colData, design = formula"
    )

    # Building command line
    dds_command <- base::paste0(
        "DESeq2::DESeqDataSetFromTximport(",
        dds_parameters,
        ")"
    )

# Case user provides a RangesSummarizedExperiment object
} else if ("se" %in% base::names(x = snakemake@input)) {
    # Loading RangedSummarizedExperiment object
    se <- base::readRDS(file = snakemake@input[["se"]])

    # Acquiring user-defined optional parameters
    dds_parameters <- add_extra(
        wrapper_defined = "se = se, design = formula, ignoreRank = FALSE"
    )

    # Building command line
    dds_command <- base::paste0(
        "DESeq2::DESeqDataSet(",
        dds_parameters,
        ")"
    )

# Case user provides HTSeq-Count/Feature-Count input files
} else if ("htseq_dir" %in% base::names(x = snakemake@input)) {
    # Casting path in case it contains only numbers
    hts_dir <- base::as.character(x = snakemake@input[["htseq_dir"]])
    base::message(hts_dir)

    # Loading sample table, and casting factors
    sample_table <- utils::read.table(
        file = snakemake@input[["sample_table"]],
        sep = "\t",
        header = TRUE,
        stringsAsFactors = TRUE
    )

    # The columns `sampleName` and `fileName`
    # are expected to be characters, while the rest
    # (if any) is supposed to be factors.
    sample_table$sampleName <- base::lapply(
        sample_table$sampleName, base::as.character
    )
    sample_table$fileName <- base::lapply(
        sample_table$fileName, base::as.character
    )

    # Acquiring user-defined optional parameters
    dds_parameters <- add_extra(
        "sampleTable = sample_table, directory = hts_dir, design = formula"
    )

    # Building command line
    dds_command <- base::paste0(
        "DESeq2::DESeqDataSetFromHTSeqCount(",
        dds_parameters,
        ")"
    )

# Case user provides an R count matrix as input
} else if ("matrix" %in% base::names(x = snakemake@input)) {
    if (base::is.null(colData)) {
        base::stop(
            "When a R `matrix` is provided in input,",
            " then a `colData` is expected"
        )
    }

    # Loading RangedSummarizedExperiment object
    count_matrix <- base::readRDS(file = snakemake@input[["matrix"]])
    base::print(head(count_matrix))


    # Acquiring user-defined optional parameters
    dds_parameters <- add_extra(
        "countData = count_matrix, colData = colData, design = formula"
    )

    # Building command line
    dds_command <- base::paste0(
        "DESeq2::DESeqDataSetFromMatrix(",
        dds_parameters,
        ")"
    )

# Case user provides a TSV count matrix as input
} else if ("counts" %in% base::names(x = snakemake@input)) {
    if (base::is.null(colData)) {
        base::stop(
            "When `counts` are provided in input, then a `colData` is expected"
        )
    }

    # Loading count table
    count_matrix <- utils::read.table(
        file = snakemake@input[["counts"]],
        header = TRUE,
        se = "\t",
        row.names = 1,
        stringsAsFactors = FALSE
    )
    base::print(head(count_matrix))

    # Acquiring user-defined optional parameters
    dds_parameters <- add_extra(
        "countData = count_matrix, colData = colData, design = formula"
    )

    # Building command line
    dds_command <- base::paste0(
        "DESeq2::DESeqDataSetFromMatrix(",
        dds_parameters,
        ")"
    )

# Case user provides a DDS object to filter
} else if ("dds" %in% base::names(x = snakemake@input)) {
    # Loading count table
    dds_path <- base::as.character(
        x = snakemake@input[["dds"]]
    )

    # Building command line
    dds_command <- "base::readRDS(file = dds_path)"
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
        dds[[factor_name]], levels = levels
    )
    dds[[factor_name]] <- stats::relevel(
        dds[[factor_name]], ref = reference_name
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
} else {
    base::message(
        "No relevel performed, since either `factor`, `reference_level`,",
        " and/or `tested_level` are missing in `snakemake@params`."
    )
}

# Dropping null counts (or below threshold) on user demand
if ("min_count" %in% base::names(x = snakemake@params)) {
    # Casting count filter since integer/numeric cannot be compared
    # to double, and other number-like types in R (depending on R version)
    count_filter <- base::as.double(x = snakemake@params[["min_count"]])
    base::message(
        "Genes with less than ",
        count_filter,
        " estimated/counted reads are filtered out."
    )
    keep <- rowSums(counts(dds)) >= count_filter
    dds <- dds[keep, ]
} else {
    base::message(
        "No count filtering performed since `min_count` is missing ",
        "in `snakemake@params`"
    )
}

# Saving DESeqDataSet object
base::saveRDS(
    object = dds,
    file = base::as.character(x = snakemake@output[[1]])
)
base::message("DDS object saved, process over")

# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
base::sink(type = "message")
base::sink()