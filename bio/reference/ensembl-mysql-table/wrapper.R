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

library("dbplyr")
library("RMariaDB")

wanted_species <- snakemake@params[["species"]]
wanted_release <- snakemake@params[["release"]]
wanted_build <- snakemake@params[["build"]]

main_tables <- snakemake@params[["main_tables"]]
join_tables <- snakemake@params[["join_tables"]]

output_filename <- snakemake@output[["table"]]

if (wanted_build == "GRCh37") {
  port <- 3337
} else if (wanted_build == "GRCm38") {
  if (wanted_release > 99) {
    cli_abort(c(
            "From Ensembl release 100 and upwards, genome build GRCm38 is not available any more.",
      "i" = "Please choose a release of 99 or lower, or choose a newer mouse genome build.",
    ))
  }
  port <- 3337
} else {
  port <- 3306
}

# general connection to ensembl databases
ensembl_connection <- dbConnect(
  MariaDB(),
  host = "ensembldb.ensembl.org", 
  user = "anonymous",
  port = port,
  password = "",
  timeout=45
)

get_and_check_db_name <- function(connection, species, database, release, wanted_build) {
  dbname_prefix <- str_c(
    species,
    database,
    release,
    sep ="_"
  )
  dbname <- dbGetQuery(connection, "SHOW DATABASES") |> filter(str_starts(Database, dbname_prefix))

  if ( length(dbname) == 1 ) {
    retrieved_build_num <- dbname |> first() |> str_split("_") |> first() |> last()
    # Canonicalize the build number to a single number as used in the mysql
    # database names. At the time of writing, this code fails for 20 species,
    # but build/assembly name numbers in those have no systematic relationship
    # with the build numbers used in the respective mysql databases. Thus, we
    # throw an error in those cases and ask users to check up the correct
    # matchup manually.
    wanted_build_num <- wanted_build |>
      # remove patch suffixes like ".p14" in "GRCh38.p14", although usually
      # we expect users of the wrapper to only specify "GRCh38" as the build
      str_replace("\\.p\\d+$", "") |>
      # look for trailing combinations of digits and dots
      str_extract("[\\d\\.]+$") |>
      # remove all dots, as mysql database numbers contain no dots
      str_replace_all( "\\.", "") |>
      # remove leading zeros, for example from "PKINGS_0.1"
      str_replace( "^0+", "") |>
      # remove trailing zeros, as this is needed for the vast majority of such
      # cases (but in some cases this causes a mismatch, but there is no
      # systematic way of resolving when)
      str_replace("0$", "")

    if (retrieved_build_num != wanted_build_num) {
      # Systematic extraction didn't match up. We'll try matching up by downloading
      # the releases species summary file from the FTP servers. ¯\_(ツ)_/¯
      species_file_address <- str_c(
        "https://ftp.ensembl.org/pub/release-",
        release,
        "/species_EnsemblVertebrates.txt"
      )
      species_summary <- read_tsv(species_file_address) |>
        filter( str_starts(core_db, species) ) |>
        select(assembly, core_db)
      assembly <- species_summary |> pull(assembly) |> first()
      summary_build_num <- species_summary |> pull(core_db) |> first() |> str_split("_") |> first() |> last()
      if ( (! str_starts(wanted_build, assembly)) & (summary_build_num != wanted_build_num) ) {
        cli_abort(c(
                "The build we could retrieve for the specified combination of species, database, and release does",
                " not match the build you specified.",
          "x" = "Genome build '{wanted_build}' requested for species '{species}' at Ensembl release '{release}', but",
          " " = "only found build with number '{retrieved_build_num}'. This does not match the build number we",
          " " = "systematically extracted from '{wanted_build}', which is '{wanted_build_num}'. We also checked",
          " " = "against the Ensembl species summary file at:",
          " " = "{species_file_address}",
          " " = "It listed the following info, which doesn't match the wanted build specification:",
          "*" = "build / assembly : '{assembly}'",
          "*" = "build number for core_db: '{summary_build_num}'",
          "i" = "Please ensure that you specify an existing combination of species, build and release.",
          " " = "The above listed species summary file is a good starting point."
        ))
      }
    }
    dbname |> pull(Database) |> first()
  } else {
    cli_abort(c(
            "Could not retrieve a (unique?) database name for the specified combination of species, database, release, and build.",
      "x" = "You requested species '{species}', database '{database}', Ensembl release '{release}', and",
      " " = "genome build '{wanted_build}'. As builds are simple numbers in the mysql database names, we",
      " " = "looked for a database with prefix '{dbname_prefix}'. Here's what we found (can be empty):",
      " " = "{dbname}",
      "i" = "Please ensure that you specify an existing and unique combination of species, database, release, and build.",
      " " = "The following species summary file can be a good starting point:",
      " " = "https://ftp.ensembl.org/pub/release-{release}/species_EnsemblVertebrates.txt"
    ))
  }
}

get_table <- function(dbname, port, table_name) {
  table_connection <- dbConnect(
    MariaDB(),
    dbname = dbname,
    host = "ensembldb.ensembl.org", 
    user = "anonymous",
    port = port,
    password = "",
    timeout=45
  )
  table <- tbl(table_connection, table_name) |> collect()
  table
}

main_table <- tibble()
for (table in names(main_tables)) {
  main_table_db_name <- get_and_check_db_name(ensembl_connection, wanted_species, main_tables[[table]], wanted_release, wanted_build)
  main_table <- main_table |>
    bind_rows(
      get_table(main_table_db_name, port, table)
    )
}

if ( !is.null(join_tables) ) {
  for (table in names(join_tables)) {
    table_db_name <- get_and_check_db_name(ensembl_connection, wanted_species, join_tables[[table]][["database"]], wanted_release, wanted_build)
    tbl <- get_table(table_db_name, port, table)
    main_table <- main_table |>
      left_join(
        tbl,
        by = join_tables[[table]][["join_column"]]
      )
  }
}

if ( str_detect(output_filename, "tsv(\\.(gz|bz2|xz))?$") ) {
  write_tsv(
    x = main_table,
    file = output_filename
  )
} else if ( str_detect(output_filename, "\\.parquet") ) {
  last_ext <- path_ext(output_filename)
  compression <- case_match(
    last_ext,
    "parquet" ~ "uncompressed",
    "gz" ~ "gzip",
    "zst" ~ "zstd",
    "sz" ~ "snappy"
  )
  if ( is.na(compression) ) {
    cli_abort(
            "File extension '{last_ext}' not supported for writing with the used nanoparquet version.",
      "x" = "Cannot write to a file '{output_filename}', because the version of the package",
            "nanoparquet used does not support writing files of type '{last_ext}'.",
      "i" = "For supported file types, see: https://r-lib.github.io/nanoparquet/reference/write_parquet.html"
    )
  }
  write_parquet(
    x = main_table,
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
