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
base::message("Saving plot to file: ")
base::print(out_pdf)


# Set parameters
params <- list("label" = ifelse("label" %in% base::names(snakemake@params), snakemake@params[["label"]], NA),
               "labels" = NA,
               "col" = NA,
               "enforce_consistency" = ifelse("enforce_consistency" %in% base::names(snakemake@params), as.logical(snakemake@params[["enforce_consistency"]]), FALSE),
               "star" = ifelse("star" %in% base::names(snakemake@params), snakemake@params[["star"]], 95),
               "correction_factor" = ifelse("correction_factor" %in% base::names(snakemake@params), as.logical(snakemake@params[["correction_factor"]]), FALSE),
               "weights_exp" = NA,
               "skip_model" = ifelse("skip_model" %in% base::names(snakemake@params), as.logical(snakemake@params[["skip_model"]]), FALSE)
              )

# Not sure why, by using "ifelse" only keeps the first element of the vector
if ("labels" %in% base::names(snakemake@params)) {
   params[["labels"]] = unlist(strsplit(snakemake@params[["labels"]], ","))
   }

if ("col" %in% base::names(snakemake@params)) {
   params[["col"]] = unlist(strsplit(snakemake@params[["col"]], ","))
   }

if ("weights_exp" %in% base::names(snakemake@params)) {
   params[["weights_exp"]] = as.numeric(unlist(strsplit(snakemake@params[["weights_exp"]], ",")))
   }

base::message("Options provided:")
utils::str(params)


# Infer model
pdf(out_pdf)
curves <- Nonpareil.curve.batch(in_files,
                                label = params[["label"]],
                                labels = params[["labels"]],
                                col = params[["col"]],
                                enforce.consistency = params[["enforce_consistency"]],
                                star = params[["star"]],
                                correction.factor = params[["correction_factor"]],
                                weights.exp = params[["weights_exp"]],
                                skip.model = params[["skip_model"]],
                                plot = FALSE
                                )


# Get stats
stats <- summary(curves)
# Fix names
colnames(stats) <- c("Redundancy", "Avg. coverage", "Seq. effort", "Model correlation", "Required seq. effort", "Diversity")


# If model not infered, set its values to NA
stats[,4] <- sapply(stats[,4], function(x){if(length(x) == 0){NA} else {x}})
stats[,5] <- sapply(stats[,5], function(x){if(length(x) == 0){NA} else {x}})


# Convert to Gb
stats[,3] <- stats[,3] / 1e9
stats[,5] <- stats[,5] / 1e9
# Round
stats <- round(stats, digits = 2)
# Print stats to log
base::print(stats)


# Save plot
plot(curves, legend.opts = FALSE)


# Add legend
legend("bottomright", legend = paste0(paste(colnames(stats), t(stats), sep=": "), c("",""," Gb",""," Gb","")), cex = 0.5)
if (length(in_files) > 1) {
  Nonpareil.legend(curves, "topleft", cex = 0.5)
}


# Save model
if ("model" %in% base::names(snakemake@output)) {
  save(curves, file=snakemake@output[["model"]])
}


base::message("Nonpareil plot saved")
dev.off()


# Proper syntax to close the connection for the log file
# but could be optional for Snakemake wrapper
base::sink(type = "message")
base::sink()
