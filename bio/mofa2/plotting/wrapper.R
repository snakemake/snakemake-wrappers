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

# output_path <- as.character(snakemake@output[[1]])

# load a MOFA2 model from an hdf5 file
model <- load_model(input_path)

# creating the requested plots

# overview plot
if ("overview" %in% names(snakemake@output)) {
  overview_path <- as.character(snakemake@output[["overview"]])
  p <- plot_data_overview(model)

  # write plot to file
  ggsave(filename = overview_path)
}

# variance_explained plot
if ("variance_explained" %in% names(snakemake@output)) {
  variance_explained_path <- as.character(snakemake@output[["variance_explained"]])
  p <- plot_variance_explained(model, x="view", y="factor")

  # write plot to file
  ggsave(filename = variance_explained_path)
}

# TODO: visualisation of factors

# feature weights plot
# TODO: add multiple views
if ("feature_weights" %in% names(snakemake@output)) {
  feature_weights_path <- as.character(snakemake@output[["feature_weights"]])
  p <- plot_weights(model,
    view = "view_0",
    factor = 1,
    nfeatures = 10, # number of features to highlight
    scale = TRUE,
    abs = FALSE
  )

  # write plot to file
  ggsave(filename = feature_weights_path)
}

# TODO: covariation patterns

# covariation patterns

## covariation patterns heatmap
# TODO: add multiple views, factors
if ("data_heatmap" %in% names(snakemake@output)) {
  data_heatmap_path <- as.character(snakemake@output[["data_heatmap"]])
  p <- plot_data_heatmap(model,
    view = "view_1",
    factor = 1,
    features = 20,

    cluster_rows = TRUE, cluster_cols = FALSE,
    show_rownames = TRUE, show_colnames = FALSE
  )

  # write plot to file
  ggsave(filename = data_heatmap_path)
}

## covariation patterns scatter plot
if ("data_scatter" %in% names(snakemake@output)) {
  data_scatter_path <- as.character(snakemake@output[["data_scatter"]])
  p <- plot_data_scatter(model,
    view = "view_1",
    factor = 1,
    features = 5,
    add_lm = TRUE,
    color_by = condition
  )

  # write plot to file
  ggsave(filename = data_scatter_path)
}

