# __author__ = "Filipe G. Vieira"
# __copyright__ = "Copyright 2023, Filipe G. Vieira"
# __license__ = "MIT"

# This script plots results (NPO file) from NonPareil


# Sink the stderr and stdout to the snakemake log file
# https://stackoverflow.com/a/48173272
log.file <- file(snakemake@log[[1]], open = "wt")
base::sink(log.file)
base::sink(log.file, type = "message")


# Loading libraries (order matters)
base::library(package = "Nonpareil", character.only = TRUE)
base::message("Libraries loaded")


params <- list("label" = ifelse("label" %in% base::names(snakemake@params), snakemake@params[["label"]], NA),
       	       "col" = ifelse("col" %in% base::names(snakemake@params), snakemake@params[["col"]], NA),
	       "enforce_consistency" = ifelse("enforce_consistency" %in% base::names(snakemake@params), as.logical(snakemake@params[["enforce_consistency"]]), FALSE),
	       "star" = ifelse("star" %in% base::names(snakemake@params), snakemake@params[["star"]], 95),
	       "correction_factor" = ifelse("correction_factor" %in% base::names(snakemake@params), as.logical(snakemake@params[["correction_factor"]]), FALSE),
	       "weights_exp" = NA,
	       "skip_model" = ifelse("skip_model" %in% base::names(snakemake@params), as.logical(snakemake@params[["skip_model"]]), FALSE)
	      )

# Not sure why, by using "ifelse" only keeps the first element of the vector
if ("weights_exp" %in% base::names(snakemake@params)) {
   params[["weights_exp"]] = as.numeric(unlist(strsplit(snakemake@params[["weights_exp"]], ",")))
   }


base::message("Options provided:")
base::print(params)


pdf(snakemake@output[[1]])
Nonpareil.curve(file = snakemake@input[[1]],
		label = params[["label"]],
		col = params[["col"]],
		enforce.consistency = params[["enforce_consistency"]],
		star = params[["star"]],
		correction.factor = params[["correction_factor"]],
		weights.exp = params[["weights_exp"]],
		skip.model = params[["skip_model"]]
	       )


base::message("Nonpareil plot saved")
dev.off()


# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
base::sink(type = "message")
base::sink()
