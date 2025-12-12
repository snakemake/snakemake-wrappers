#!/bin/R

# Loading library
library(MOFA2)
library(arrow)

# load long.data frame from parquet file with headers
# `sample, feature, view, group (optional), value`

# cast input path as character to avoid errors
path <- as.character(snakemake@input[[1]])

df <- read_parquet(path)

mofa_object <- create_mofa(df)

data_opts <- get_default_data_options(mofa_object)
model_opts <- get_default_model_options(mofa_object)
train_opts <- get_default_training_options(mofa_object)

mofa_object <- prepare_mofa(
  object = mofa_object,
  data_options = data_opts,
  model_options = model_opts,
  training_options = train_opts
)

outfile <- file.path(getwd(), snakemake@output[[1]])

# train the MOFA model and write the result to `outfile`
run_mofa(mofa_object, outfile)
