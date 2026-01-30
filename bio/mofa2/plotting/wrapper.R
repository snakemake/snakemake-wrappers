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

# load a MOFA2 model from an hdf5 file
model <- load_model(input_path)


# setting the variables customisable with params

if ("view" %in% names(snakemake@params)) {
  view <- snakemake@params[["view"]]
} else {
  view <- "view_0"
}

if ("factor" %in% names(snakemake@params)) {
  factor <- snakemake@params[["factor"]]
} else {
  factor <- 1
}

if ("features" %in% names(snakemake@params)) {
  features <- snakemake@params[["features"]]
} else {
  features <- 10
}

if ("nfeatures" %in% names(snakemake@params)) {
  nfeatures <- snakemake@params[["nfeatures"]]
} else {
  nfeatures <- 10
}

# creating the requested plots

# overview plot
if ("overview" %in% names(snakemake@output)) {
  overview_path <- as.character(snakemake@output[["overview"]])
  p <- plot_data_overview(model)

  # write plot to file
  ggsave(plot = p, filename = overview_path)
}

# variance_explained plot
if ("variance_explained" %in% names(snakemake@output)) {
  variance_explained_path <- as.character(snakemake@output[["variance_explained"]])
  p <- plot_variance_explained(model, x="view", y="factor")

  # write plot to file
  ggsave(plot = p, filename = variance_explained_path)
}

# feature weights plot
if ("feature_weights" %in% names(snakemake@output)) {
  feature_weights_path <- as.character(snakemake@output[["feature_weights"]])
  p <- plot_weights(model,
    view = view, # which view to plot
    factor = factor, # which factor to plot
    nfeatures = nfeatures, # number of features to highlight
    scale = TRUE, # scale weights from -1 to 1
    abs = FALSE # take the absolute value?
  )

  # write plot to file
  ggsave(plot = p, filename = feature_weights_path)
}

# covariation patterns

## covariation patterns heatmap
if ("data_heatmap" %in% names(snakemake@output)) {
  data_heatmap_path <- as.character(snakemake@output[["data_heatmap"]])
  p <- plot_data_heatmap(model,
    view = view, # which view to plot
    factor = factor, # which factor to plot
    features = features, # how many features to plot

    cluster_rows = TRUE, cluster_cols = FALSE,
    show_rownames = TRUE, show_colnames = FALSE
  )

  # write plot to file
  ggsave(plot = p, filename = data_heatmap_path)
}

