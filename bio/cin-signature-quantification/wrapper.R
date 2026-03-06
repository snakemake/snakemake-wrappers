#!/bin/R

# load libraries
library(CINSignatureQuantification)
library(tibble)
library(dplyr)
library(tidyr)
library(stringr)
library(arrow)

# cast input path and param as character to avoid errors
input_path <- as.character(snakemake@input[[1]])
experiment_name <- as.character(snakemake@params[["experiment_name"]])

# cast thread count as integer to avoid errors

cores <- as.integer(snakemake@threads)

# load data

data(input_path)

cnobj <- quantifyCNSignatures(
  object = input_path,
  experimentName = experiment_name,
  method = "dres",
  cores = cores,
  build = "hg19"
)

if ("cnobj" %in% names(snakemake@output)) {
  path <- as.character(snakemake@output[["cnobj"]])
  saveRDS(cnobj, file = path)
}

# features

if ("features" %in% names(snakemake@output)) {
  feature_path <- as.character(snakemake@output[["features"]])
  feats <- getFeatures(cnobj)
  dfs <- feats |>
    lapply(function(df) {
      names(df)[2] <- "value"
      df
    })
  df <- bind_rows(dfs, .id = "feature")
  df |> select(ID, feature, value) |> write_parquet(feature_path)
}

# signature activities

if ("signature_activities" %in% names(snakemake@output)) {
  sig_path <- as.character(snakemake@output[["signature_activities"]])

  sigAct <- getActivities(cnobj, type = "threashold")

  # transform from matrix to data.frame in tidy format

  df <- sigAct |>
    as.data.frame() |>
    rownames_to_column("sample") |>
    pivot_longer(-"sample", names_to = "signature", values_to = "value")

  write_parquet(df, sig_path)
}

# sample by component

if ("sample_by_component" %in% names(snakemake@output)) {
  sxc_path <- as.character(snakemake@output[["sample_by_component"]])

  SxC <- getSampleByComponen(cnobj)

  # transform from matrix to data.frame in tidy format

  df <- SxC |>
    as.data.frame() |>
    rownames_to_column("sample") |>
    pivot_longer(-"sample", names_to = "component", values_to = "value")

  write_parquet(df, sxc_path)
}

# clinical predictors

if ("clinical_predictors" %in% names(snakemake@output)) {
  clin_pred_path <- as.character(snakemake@output[["clinical_predictors"]])

  pred <- clinPredictionPlatinum(object = cnobj)
  df <- enframe(pred, name = "sample", value = "prediction")
  df <- df |> mutate(prediction = str_replace(prediction, "Predicted ", ""))
  
  write_parquet(df, clin_pred_path)
}
