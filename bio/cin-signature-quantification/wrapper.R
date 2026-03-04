#!/bin/R

# load libraries
library(CINSignatureQuantification)

# cast input and output path as character to avoid errors
input_path <- as.character(snakemake@input[[1]])

# load data

data(input_path)
