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

# Collapse path into a character vector
samples_paths <- base::paste0(samples_paths, collapse = '", "');

# Building function arguments
extra <- base::paste0('files = c("', samples_paths, '")');

# Check if user provided optional transcript to gene table
if ("tx_to_gene" %in% names(snakemake@input)) {
  tx2gene <- readr::read_tsv(snakemake@input[["tx_to_gene"]]);
  extra <- base::paste(
    extra,                 # Foreward existing arguments
    ", tx2gene = ",        # Argument name
    "tx2gene"              # Add tx2gene to parameters
  );
}

# Add user defined arguments
if ("extra" %in% names(snakemake@params)) {
  if (snakemake@params[["extra"]] != "") {
    extra <- base::paste(
      extra,                       # Foreward existing parameters
      snakemake@params[["extra"]], # Add user parameters
      sep = ", "                   # Field separator
    );
  }
}


print(extra);
# Perform tximport work
txi <- base::eval(                        # Evaluate the following
  base::parse(                            # ... parsed expression
    text = base::paste0(
      "tximport::tximport(", extra, ");"  # ... of tximport and its arguments
    )
  )
);

# Save results
base::saveRDS(                       # Save R object
  object = txi,                      # The txi object
  file = snakemake@output[["txi"]]   # Output path is provided by Snakemake
);
