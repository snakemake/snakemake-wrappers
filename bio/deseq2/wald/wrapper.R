# This script takes a deseq2 dataset object, performs
# a DESeq2 wald test, and saves results as requested by user

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
base::library(package = "BiocParallel", character.only = TRUE)
base::library(package = "SummarizedExperiment", character.only = TRUE)
base::library(package = "DESeq2", character.only = TRUE)
base::library(package = "ashr", character.only = TRUE)

# Function to handle optional user-defined parameters
# and still follow R syntax
add_extra <- function(wrapper_extra, snakemake_param_name) {
  if (snakemake_param_name %in% base::names(snakemake@params)) {
    # Case user provides snakemake_param_name in snakemake rule
    user_param <- snakemake@params[[snakemake_param_name]]

    param_is_empty <- user_param == ""
    param_is_character <- inherits(x = user_param, what = "charcter")
    if ((! param_is_empty) && (param_is_character)) {
      # Case user do not provide an empty string
      # (R does not like trailing commas at the end
      # of a function call)
      wrapper_extra <- base::paste(
        wrapper_extra,
        user_param,
        sep = ", "
      )
    } # Nothing to do if user provides an empty / NULL parameter value
  } # Nothing to do if user did not provide snakemake_param_name

  # In any case, required parameters must be returned
  base::return(wrapper_extra)
}

# Setting up multithreading if required
parallel <- FALSE
if (snakemake@threads > 1) {
    BiocParallel::register(
      BPPARAM = BiocParallel::MulticoreParam(snakemake@threads)
    )
    parallel <- TRUE
}

# Load DESeq2 dataset
dds_path <- base::as.character(x = snakemake@input[["dds"]])
dds <- base::readRDS(file = dds_path)
base::message("Libraries and dataset loaded")

# Build extra parameters for DESeq2
extra_deseq2 <- add_extra(
  wrapper_extra = "object = dds, test = 'Wald', parallel = parallel",
  snakemake_param_name = "deseq_extra"
)

deseq2_cmd <- base::paste0(
  "DESeq2::DESeq(", extra_deseq2, ")"
)
base::message("DESeq2 command line:")
base::message(deseq2_cmd)

# Running DESeq2::DESeq for wald test result
wald <- base::eval(base::parse(text = deseq2_cmd))


# The rest of the script is here to save part or complete
# list of results in RDS or plain text (TSV) formats.


# Save main result on user request (RDS)
# This includes counts, wald tests for all levels
# assays, design, etc.
if ("wald_rds" %in% base::names(x = snakemake@output)) {
  output_rds <- base::as.character(x = snakemake@output[["wald_rds"]])
  base::saveRDS(obj = wald, file = output_rds)
  base::message("Wald test saved as RDS file")
}

# Saving normalized counts on demand
table <- counts(wald)

# TSV-formatted count table
if ("normalized_counts_table" %in% base::names(snakemake@output)) {
  output_table <- base::as.character(
    x = snakemake@output[["normalized_counts_table"]]
  )
  utils::write.table(x = table, file = output_table, sep = "\t", quote = FALSE)
  base::message("Normalized counts saved as TSV")
}

# RDS-formated count object with many information,
# including counts, assays, etc.
if ("normalized_counts_rds" %in% base::names(snakemake@output)) {
  output_rds <- base::as.character(
    x = snakemake@output[["normalized_counts_rds"]]
  )
  base::saveRDS(obj = table, file = output_rds)
  base::message("Normalized counts saved as RDS")
}

# On user request: save all results as TSV in a directory.
# User can later access the directory content, e.g. with
# a snakemake checkpoint-rule.
if ("deseq2_result_dir" %in% base::names(snakemake@output)) {
  # Acquire list of available results in DESeqDataSet
  wald_results_names <- DESeq2::resultsNames(object = wald)

  # Recovering extra parameters for TSV tables
  # The variable `result_name` is built below in `for` loop.
  results_extra <- add_extra(
    wrapper_extra = "object = wald, name = result_name, parallel = parallel",
    snakemake_param_name = "results_extra"
  )

  # DESeq2 result dir will contain all results available in the Wald object
  output_prefix <- snakemake@output[["deseq2_result_dir"]]
  if (! base::file.exists(output_prefix)) {
    base::dir.create(path = output_prefix, recursive = TRUE)
  }

  # Building command lines for both wald results and fc schinkage
  results_cmd <- base::paste0("DESeq2::results(", results_extra, ")")
  base::message("Command line used for TSV results creation:")
  base::message(results_cmd)

  shrink_extra <- add_extra(
    "dds = wald, res = results_frame, contrast = contrast, parallel = parallel, type = 'ashr'",
    "shrink_extra"
  )
  shrink_cmd <- base::paste0("DESeq2::lfcShrink(", shrink_extra, ")")
  base::message("Command line used for log(FC) shrinkage:")
  base::message(shrink_cmd)

  # For each available comparison in the wald-dds object
  for (result_name in wald_results_names) {
    # Building table
    base::message(base::paste("Saving results for", result_name))
    results_frame <- base::eval(base::parse(text = results_cmd))
    shrink_frame <- base::eval(base::parse(text = shrink_cmd))
    results_frame$log2FoldChange <- shrink_frame$log2FoldChange

    results_path <- base::file.path(
      output_prefix,
      base::paste0(result_name, ".tsv")
    )

    # Saving table
    utils::write.table(
      x = results_frame,
      file = results_path,
      quote = FALSE,
      sep = "\t",
      row.names = TRUE
    )
  }
}


# If user provides contrasts, then a precise result
# can be extracted from DESeq2 object.
if ("wald_tsv" %in% base::names(x = snakemake@output)) {
  if ("contrast" %in% base::names(x = snakemake@params)) {
    contrast_length <- base::length(x = snakemake@params[["contrast"]])

    results_extra <- "object=wald, parallel = parallel"
    contrast <- NULL

    if (contrast_length == 1) {
      # Case user provided a result name in the `contrast` parameter
      contrast <- base::as.character(x = snakemake@params[["contrast"]])
      contrast <- base::paste0("name='", contrast[1], "'")

    } else if (contrast_length == 2) {
      # Case user provided both tested and reference level
      # In that order! Order matters.
      contrast <- sapply(
        snakemake@params[["contrast"]],
        function(extra) base::as.character(x = extra)
      )
      contrast <- base::paste0(
        "contrast=list('", contrast[1], "', '", contrast[2], "')"
      )

    } else if (contrast_length == 3) {
      # Case user provided both tested and reference level,
      # and studied factor.
      contrast <- sapply(
        snakemake@params[["contrast"]],
        function(extra) base::as.character(x = extra)
      )
      contrast <- base::paste0(
        "contrast=c('",
        contrast[1],
        "', '",
        contrast[2],
        "', '",
        contrast[3],
        "')"
      )

      # Finally saving results as contrast has been
      # built from user input.
      results_extra <- base::paste(results_extra, contrast, sep = ", ")
      results_cmd <- base::paste0("DESeq2::results(", results_extra, ")")
      base::message("Result extraction command: ", results_cmd)

      shrink_extra <- add_extra(
        "dds = wald, res = results_frame, contrast = contrast[1], parallel = parallel, type = 'ashr'",
        "shrink_extra"
      )
      shrink_cmd <- base::paste0("DESeq2::lfcShrink(", shrink_extra, ")")
      base::message("Command line used for log(FC) shrinkage:")
      base::message(shrink_cmd)


      results_frame <- base::eval(base::parse(text = results_cmd))
      shrink_frame <- base::eval(base::parse(text = shrink_cmd))
      results_frame$log2FoldChange <- shrink_frame$log2FoldChange

      # Saving table
      utils::write.table(
        x = results_frame,
        file = base::as.character(x = snakemake@output[["wald_tsv"]]),
        quote = FALSE,
        sep = "\t",
        row.names = TRUE
      )
    }
  } else {
    base::stop(
      "No contrast provided. ",
      "In absence of contrast, it is not possible ",
      "to guess the expected result name.",
    )
  }
}

# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
base::sink(type = "message")
base::sink()