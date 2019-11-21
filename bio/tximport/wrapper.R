#!/bin/R

# Loading library
base::library("tximport");   # Perform actual count importation in R
base::library("readr");      # Read faster!
base::library("jsonlite");   # Importing inferential replicates

# Cast input paths as character to avoid errors
samples_paths <- sapply(               # Sequentially apply
  snakemake@input[["quant"]],          # ... to all quantification paths
  function(quant) as.character(quant)  # ... a cast as character
);

# Building extra parameters for tximport
extra <- list();
for (name in names(snakemake@params)) {
  extra[[name]] = snakemake@params[[name]];
}

# Add paths to samples
extra$files = samples_paths;

if ("tx2gene" %in% names(snakemake@input)) {     # Check if user provided a tx2gene
  extra$tx2gene <- snakemake@input[["tx2gene"]]; # Add tx2gene to parameters
}

# Perform tximport work
txi <- do.call(            # Call a function with a list of args
  tximport::tximport,      # Call specifically tximport
  extra                    # Extra parameters to pass
);

# Save results
base::saveRDS(                       # Save R object
  object = txi,                      # The txi object
  file = snakemake@output[["txi"]]   # Output path is provided by Snakemake
);
