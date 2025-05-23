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
base::library(package = "apeglm", character.only = TRUE)

# Function to handle optional user-defined parameters
# and still follow R syntax
add_extra <- function(wrapper_extra, snakemake_param_name) {
  if (snakemake_param_name %in% base::names(snakemake@params)) {
    # Case user provides snakemake_param_name in snakemake rule
    user_param <- snakemake@params[[snakemake_param_name]]
    base::message(user_param)
    base::message(wrapper_extra)

    if (! user_param == "") {
      # Case user do not provide an empty value
      # (R does not like trailing commas at the end
      # of a function call)
      wrapper_extra <- base::paste(
        wrapper_extra,
        base::as.character(x = user_param),
        sep = ", "
      )
    } # Nothing to do if user provides an empty / NULL parameter value
  } # Nothing to do if user did not provide snakemake_param_name

  # In any case, required parameters must be returned
  base::return(wrapper_extra)
}


# A result name is build using the following template
# {factor}_{tested}_vs_{ref}
get_result_name_from_params <- function(contrast_vector, dds) {
  # Instantiate to null in order to let DESeq2 raise an error if user provided
  # contrast_vector does not fit DESeq2 standards
  name <- NULL
  contrast_length <- base::length(contrast_vector)

  if (contrast_length == 1) {
    name <- contrast_vector[1]
  } else if (contrast_length == 2) {
    # There may be ambguity here with factors having identical level names
    # The suffix of the expected result:
    suffix <- base::paste(
      contrast_vector[2], "vs", contrast_vector[1], sep = "_"
    )
    names <- DESeq2::resultsNames(dds)
    # All possible results matchig this suffix
    names <- names[base::endsWith(names, suffix)]
    if (! base::length(names) == 1) {
      base::stop(
        "Could not guess correct result name from contrast ",
        "due to the following ambiguity:",
        base::paste(DESeq2::resultsNames(dds), sep = " "),
        " based on the following suffix: ",
        suffix
      )
    }
    # Case there is no abiguity:
    name <- names[1]
  } else if (contrast_length == 3) {
    name <- base::paste(
      contrast_vector[1],
      contrast_vector[3],
      "vs",
      contrast_vector[2],
      sep = "_"
    )
  }

  base::return(name)
}


# Function to address concerns about `coef` used in `apeglm` package
get_coef_from_dds_and_params <- function(contrast_vector, dds) {
  # Set to null in order to raise an explicit error in DESeq2
  coef <- NULL
  results_names <- DESeq2::resultsNames(dds)
  name <- get_result_name_from_params(contrast_vector, dds)
  # Raising eror with message since the later command
  # would fail before DESeq2 could raise any error.
  if (! name %in% results_names) {
    base::stop(
      "Couldn't find resultName: ",
      name,
      " within ",
      base::paste(results_names)
    )
  }
  coef <- base::which(results_names == name)
  base::return(coef)
}


# Fill parameters for lfcShrink
lfc_shrink_additional_parameters <- function(shrink_extra, coef, name) {
  # Acquire user-defined optional parameters
  shrink_extra <- add_extra(
    wrapper_extra = "dds = wald, parallel = parallel",
    snakemake_param_name = "shrink_extra"
  )

  # Add coef to access results easily
  if (base::grepl(pattern = "apeglm", x = shrink_extra, fixed = TRUE)) {
    shrink_extra <- base::paste0(shrink_extra, ", coef=", coef)
  } else {
    shrink_extra <- base::paste0(shrink_extra, ", coef=", name)
  }

  base::return(shrink_extra)
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

# Ensure future "paste" command work
contrast_vector <- base::sapply(
  snakemake@params[["contrast"]],
  function(extra) base::as.character(x = extra)
)

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

  # DESeq2 result dir will contain all results available in the Wald object
  output_prefix <- snakemake@output[["deseq2_result_dir"]]
  if (! base::file.exists(output_prefix)) {
    base::dir.create(path = output_prefix, recursive = TRUE)
  }

  # Building command lines for wald results
  #
  # The variable `result_name` is declared here, but evaluated
  # later in the for loop.
  results_extra <- add_extra(
    wrapper_extra = "object = wald, name = result_name, parallel = parallel",
    snakemake_param_name = "results_extra"
  )

  results_cmd <- base::paste0("DESeq2::results(", results_extra, ")")
  base::message("Command line used for TSV results creation:")
  base::message(results_cmd)



  # For each available comparison in the wald-dds object
  for (result_name in wald_results_names) {
    # Setting all the lfcShrink values using resultsName
    # in order to always shrink the correct result and not
    # the one listed in 'snakemake@params[["contrast"]]'
    #
    # However, the argument names must be adjusted to
    # the shrinkage method requested by user
    coef <- get_coef_from_dds_and_params(c(result_name), wald)
    name <- base::paste0("'", result_name, "'")

    shrink_extra <- lfc_shrink_additional_parameters(
      shrink_extra = snakemake@params[["shrink_extra"]],
      coef = coef,
      name = name
    )

    # Apeglm does not accept to correct intercept. It raises an error
    # if coef == 1. This factor is skipped and all other results are
    # iteratively saved on disk
    if ((! (base::grepl("ashr", shrink_extra)) || ( base::grepl("normal", shrink_extra))) && (coef < 2)) {
      base::message(
        "Cannot run `apeglm` on `",
        result_name,
        "`, since it's coef is `",
        coef,
        "`. Skipping."
      )
    } else {
      shrink_cmd <- base::paste0("DESeq2::lfcShrink(", shrink_extra, ")")
      base::message("Command line used for log(FC) shrinkage:")
      base::message(shrink_cmd)


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
}


# If user provides contrasts, then a precise result
# can be extracted from DESeq2 object.
if ("wald_tsv" %in% base::names(x = snakemake@output)) {
  if ("contrast" %in% base::names(x = snakemake@params)) {
    # Define all `contrast`, `coef`, and `name` to prepare
    # to any shrinkage parameter set by user and still focus
    # on the provided contrast given in `snakemake@params[["contrast"]]`
    name <- get_result_name_from_params(contrast_vector, wald)
    coef <- get_coef_from_dds_and_params(contrast_vector, wald)


    # Finally saving results as contrast has been
    # built from user input.
    # Extracting results:
    results_extra <- add_extra(
      wrapper_extra = "object = wald, name = name, parallel = parallel",
      snakemake_param_name = "results_extra"
    )
    results_cmd <- base::paste0("DESeq2::results(", results_extra, ")")
    base::message("Result extraction command: ", results_cmd)
    results_frame <- base::eval(base::parse(text = results_cmd))

    # Shrinking:
    shrink_extra <- lfc_shrink_additional_parameters(
      shrink_extra = snakemake@params[["shrink_extra"]],
      coef = coef,
      name = base::paste0("'", name, "'")
    )
    shrink_cmd <- base::paste0("DESeq2::lfcShrink(", shrink_extra, ")")
    base::message("Command line used for log(FC) shrinkage:")
    base::message(shrink_cmd)
    shrink_frame <- base::eval(base::parse(text = shrink_cmd))

    # Updating results:
    results_frame$log2FoldChange <- shrink_frame$log2FoldChange

    # Saving table
    utils::write.table(
      x = results_frame,
      file = base::as.character(x = snakemake@output[["wald_tsv"]]),
      quote = FALSE,
      sep = "\t",
      row.names = TRUE
    )
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
