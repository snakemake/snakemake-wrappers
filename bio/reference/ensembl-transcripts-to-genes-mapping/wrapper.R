# __author__ = "David Lähnemann"
# __copyright__ = "Copyright 2024, David Lähnemann"
# __email__ = "david.laehnemann@hhu.de"
# __license__ = "MIT"

log <- file(snakemake@log[[1]], open="wt")
sink(log)
sink(log, type="message")

library("tidyverse")
rlang::global_entrace()
library("cli")

library("biomaRt")

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

wanted_extra_columns <- snakemake@params[["extra_columns"]]

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

get_mart <- function(species, build, version, grch, dataset) {
  mart <- useEnsembl(
    biomart = "genes",
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

gene_ensembl <- get_mart(wanted_species, wanted_build, version, grch, "gene_ensembl")

wanted_attributes <- c(
  "ensembl_transcript_id",
  "ensembl_gene_id",
  wanted_extra_columns
)

if ( !is.null(wanted_chromosome) ) {
  mapping <- getBM(
    attributes = wanted_attributes,
    filters = 'chromosome_name',
    values = wanted_chromosome,
    mart = gene_ensembl
  ) |> as_tibble()
} else {
  mapping <- getBM(
    attributes = wanted_attributes,
    mart = gene_ensembl
  ) |> as_tibble()
}

write_tsv(
  mapping,
  file = snakemake@output[["mapping"]]
)
