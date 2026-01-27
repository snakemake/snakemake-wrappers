#!/bin/R

# load libraries
library(MOFA2)
library(ggplot2)

# if log file is provided, write log to that file
if (length(snakemake@log) > 0) {
  log <- file(snakemake@log[[1]], open = "wt")
  sink(log)
  sink(log, type = "message")
}


# cast input and output path as character to avoid errors
input_path <- as.character(snakemake@input[[1]])

output_path <- as.character(snakemake@output[[1]])

# load a MOFA2 model from an hdf5 file
model <- load_model(input_path)

# overview plot
p <- plot_data_overview(model)

# output plot
ggsave(filename = output_path)
