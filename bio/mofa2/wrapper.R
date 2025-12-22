#!/bin/R

# load libraries
library(MOFA2)
library(arrow)

# connect to conda environment
conda_prefix <- Sys.getenv("CONDA_PREFIX")
reticulate::use_condaenv(conda_prefix)

# if log file is provided, write log to that file
if (length(snakemake@log) > 0) {
  log <- file(snakemake@log[[1]], open = "wt")
  sink(log)
  sink(log, type = "message")
}

# load long.data frame from parquet file with following headers:
# `sample, feature, view, group (optional), value`

# cast input path as character to avoid errors
path <- as.character(snakemake@input[[1]])

df <- read_parquet(path)

mofa_object <- create_mofa(df)

data_opts <- get_default_data_options(mofa_object)
model_opts <- get_default_model_options(mofa_object)
train_opts <- get_default_training_options(mofa_object)

# add params:
# model params: scale_groups, scale_views

if ("scale_groups" %in% names(snakemake@params)) {
  if (snakemake@params[["scale_groups"]] == "FALSE") {
    data_opts$scale_groups <- FALSE
  }
  if (snakemake@params[["scale_groups"]] == "TRUE") {
    data_opts$scale_groups <- TRUE
  }
}

if ("scale_views" %in% names(snakemake@params)) {
  if (snakemake@params[["scale_views"]] == "FALSE") {
    data_opts$scale_views <- FALSE
  }
  if (snakemake@params[["scale_views"]] == "TRUE") {
    data_opts$scale_views <- TRUE
  }
}

# training params: maxiter (int), convergence_mode, gpu_mode, verbose

mofa_object <- prepare_mofa(
  object = mofa_object,
  data_options = data_opts,
  model_options = model_opts,
  training_options = train_opts
)

outfile <- file.path(getwd(), snakemake@output[[1]])

# train the MOFA model and write the result to `outfile`
run_mofa(
  mofa_object,
  outfile,
)
