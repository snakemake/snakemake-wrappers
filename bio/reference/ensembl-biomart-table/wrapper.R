# __author__ = "David Lähnemann"
# __copyright__ = "Copyright 2024, David Lähnemann"
# __email__ = "david.laehnemann@hhu.de"
# __license__ = "MIT"

log <- file(snakemake@log[[1]], open="wt")
sink(log)
sink(log, type="message")

library("tidyverse")
library("nanoparquet")
rlang::global_entrace()
library("fs")
library("cli")

library("biomaRt")

wanted_biomart <- snakemake@params[["biomart"]]
# bioconductor-biomart needs the species as something like `hsapiens` instead
# of `homo_sapiens`
wanted_species <- str_replace(
  snakemake@params[["species"]],
  "^(\\w)\\w+_(\\w+)$",
  "\\1\\2"
)
wanted_release <- snakemake@params[["release"]]
wanted_build <- snakemake@params[["build"]]

wanted_chromosome <- snakemake@params[["chromosome"]]

wanted_columns <- snakemake@params[["columns"]]

output_filename <- snakemake@output[["table"]]

if (wanted_build == "GRCh37") {
  grch <- "37"
  version <- NULL
  cli_warn(c(
    "As you specified build 'GRCH37' in your configuration yaml, biomart forces",
    "us to ignore the release you specified ('{release}')."
  ))
} else {
  grch <- NULL
  version <- wanted_release
}

get_mart <- function(biomart, species, build, version, grch, dataset) {
  mart <- useEnsembl(
    biomart = biomart,
    dataset = str_c(species, "_", dataset),
    version = version,
    GRCh = grch
  )
  
  if (build == "GRCh37") {
    retrieved_build <- str_remove(listDatasets(mart)$version, "\\..*")
  } else {
    retrieved_build <- str_remove(searchDatasets(mart, species)$version, "\\..*")
  }
  
  if (retrieved_build != build) {
    cli_abort(c(
            "The Ensembl release and genome build number you specified are not compatible.",
      "x" = "Genome build '{build}' not available via biomart for Ensembl release '{release}'.",
      "i" = "Ensembl release '{release}' only provides build '{retrieved_build}'.",
      " " = "Please fix your configuration yaml file's reference entry, you have two options:",
      "*" = "Change the build entry to '{retrieved_build}'.",
      "*" = "Change the release entry to one that provides build '{build}'. You have to determine this from biomart by yourself."
    ))
  }
  mart
}

gene_ensembl <- get_mart(wanted_biomart, wanted_species, wanted_build, version, grch, "gene_ensembl")

if ( !is.null(wanted_chromosome) ) {
  table <- getBM(
    attributes = wanted_columns,
    filters = 'chromosome_name',
    values = wanted_chromosome,
    mart = gene_ensembl
  ) |> as_tibble()
} else {
  table <- getBM(
    attributes = wanted_columns,
    mart = gene_ensembl
  ) |> as_tibble()
}


  
if ( str_detect(output_filename, "tsv(\\.(gz|bz2|xz))?$") ) {
  write_tsv(
    x = table,
    file = output_filename
  )
} else if ( str_detect(output_filename, "\\.parquet") ) {
  last_ext <- path_ext(output_filename)
  compression <- case_match(
    last_ext,
    "parquet" ~ "uncompressed",
    "gz" ~ "gzip",
    "zst" ~ "zstd",
    "sz" ~ "snappy",
    .default = cli_abort(
            "File extension '{last_ext}' not supported for writing with the used nanoparquet version.",
      "x" = "Cannot write to a file '{output_filename}', because the version of the package",
            "nanoparquet used does not support writing files of type '{last_ext}'.",
      "i" = "For supported file types, see: https://r-lib.github.io/nanoparquet/reference/write_parquet.html"
    )
  )
  write_parquet(
    x = table,
    file = output_filename, 
    compression = compression
  )
} else {
  cli_abort(c(
    "Unsupported file format in output file '{output_filename}'.",
    "x" = "Only '.tsv' and '.parquet' files are supported, with certain compression variants each.",
    "i" = "For supported compression extensions, see:",
    "*" = "tsv: https://readr.tidyverse.org/reference/write_delim.html#output",
    "*" = "parquet: https://r-lib.github.io/nanoparquet/reference/write_parquet.html#arguments"
  ))
}
