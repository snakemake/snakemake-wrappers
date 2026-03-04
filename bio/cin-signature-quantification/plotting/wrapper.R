#!/bin/R

# load libraries
library(CINSignatureQuantification)
library(tibble)
library(dplyr)
library(stringr)
library(arrow)

# cast input and output path as character to avoid errors
input_path <- as.character(snakemake@input[[1]])

# load data

data(input_path)

cnobj <- quantifyCNSignatures(
  object = input_path,
  experimentName = TODO, # specify
  method = "dres",
  cores = TODO, #specify
  build = "hg19"
)

# features
# TODO: problem: features are a list of data.frames

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

# clinical predictors

if ("clinical_predictors" %in% names(snakemake@output)) {
  clin_pred_path <- as.character(snakemake@output[["clinical_predictors"]])

  pred <- clinPredictionPlatinum(object = cnobj)
  df <- enframe(pred, name = "sample", value = "prediction")
  df <- df |> mutate(prediction = str_replace(prediction, "Predicted ", ""))
  
  write_parquet(df, clin_pred_path)
}
