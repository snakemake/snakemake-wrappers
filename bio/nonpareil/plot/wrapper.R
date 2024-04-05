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


# Set input and output files
in_files = snakemake@input[["npo"]]
out_pdf = snakemake@output[[1]]
base::message("Input files: ")
base::print(in_files)

# Set parameters
params <- list("in_files" = in_files,
               "out_pdf" = out_pdf,
               "labels" = NA,
               "col" = NA,
               "enforce_consistency" = ifelse("enforce_consistency" %in% base::names(snakemake@params), as.logical(snakemake@params[["enforce_consistency"]]), FALSE),
               "star" = ifelse("star" %in% base::names(snakemake@params), snakemake@params[["star"]], 95),
               "correction_factor" = ifelse("correction_factor" %in% base::names(snakemake@params), as.logical(snakemake@params[["correction_factor"]]), FALSE),
               "weights_exp" = NA,
               "skip_model" = ifelse("skip_model" %in% base::names(snakemake@params), as.logical(snakemake@params[["skip_model"]]), FALSE),
               "plot_observed" = ifelse("plot_observed" %in% base::names(snakemake@params), as.logical(snakemake@params[["plot_observed"]]), TRUE),
               "plot_model" = ifelse("plot_model" %in% base::names(snakemake@params), as.logical(snakemake@params[["plot_model"]]), TRUE),
               "plot_dispersion" = ifelse("plot_dispersion" %in% base::names(snakemake@params), snakemake@params[["plot_dispersion"]], FALSE),
               "plot_diversity" = ifelse("plot_diversity" %in% base::names(snakemake@params), as.logical(snakemake@params[["plot_diversity"]]), FALSE)
              )

# Not sure why, by using "ifelse" only keeps the first element of the vector
if ("labels" %in% base::names(snakemake@params)) {
   params[["labels"]] = snakemake@params[["labels"]]
   }

if ("col" %in% base::names(snakemake@params)) {
   params[["col"]] = snakemake@params[["col"]]
   }

if ("weights_exp" %in% base::names(snakemake@params)) {
   params[["weights_exp"]] = snakemake@params[["weights_exp"]]
   }

base::message("Options provided:")
utils::str(params)



##################
### Save plots ###
##################
pdf(out_pdf)
curves <- Nonpareil.set(in_files,
                        labels = params[["labels"]],
                        col = params[["col"]],
                        enforce.consistency = params[["enforce_consistency"]],
                        star = params[["star"]],
                        correction.factor = params[["correction_factor"]],
                        weights.exp = params[["weights_exp"]],
                        skip.model = params[["skip_model"]],
                        plot = FALSE
                       )

lapply(curves$np.curves, plot,
       col = params[["col"]],
       plot.observed = params[["plot_observed"]],
       plot.model = params[["plot_model"]],
       plot.dispersion = params[["plot_dispersion"]],
       plot.diversity = params[["plot_diversity"]]
)
dev.off()
base::message("Nonpareil plot saved")



##################
### Save stats ###
##################
stats <- summary(curves)
# Fix names
colnames(stats) <- c("Redundancy", "Avg. coverage", "Seq. effort", "Model correlation", "Required seq. effort", "Diversity")
# Print stats to log
base::print(stats)



##################
### Save model ###
##################
if ("model" %in% base::names(snakemake@output)) {
  save(curves, file=snakemake@output[["model"]])
}



#################
### Save JSON ###
#################
if ("json" %in% base::names(snakemake@output)) {
  base::library("jsonlite")
  base::message("Exporting model as JSON")

  export_curve <- function(object){
    # Extract variables
    n <- names(attributes(object))[c(1:12,21:29)]
    x <- sapply(n, function(v) attr(object,v))
    names(x) <- n
    # Extract vectors
    n <- names(attributes(object))[13:20]
    y <- lapply(n, function(v) attr(object,v))
    names(y) <- n
    curve_json <- c(x, y)

    # Add model
    if (object$has.model) {
      # https://github.com/lmrodriguezr/nonpareil/blob/162f1697ab1a21128e1857dd87fa93011e30c1ba/utils/Nonpareil/R/Nonpareil.R#L330-L332
      x_min <- 1e3
      x_max <- signif(tail(attr(object,"x.adj"), n=1)*10, 1)
      x.model <- exp(seq(log(x_min), log(x_max), length.out=1e3))
      y.model <- predict(object, lr=x.model)
      curve_json <- append(curve_json, list(x.model=x.model))
      curve_json <- append(curve_json, list(y.model=y.model))
    }

    base::print(curve_json)
    curve_json
  }

  export_set <- function(object){
    y <- lapply(object$np.curves, "export_curve")
    names(y) <- sapply(object$np.curves, function(n) n$label)
    jsonlite::prettify(toJSON(y, auto_unbox=TRUE))
  }

  y <- export_set(curves)
  write(y, snakemake@output[["json"]])
  base::message("JSON file saved")
}



# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
base::sink(type = "message")
base::sink()
