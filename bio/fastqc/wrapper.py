"""Snakemake wrapper for fastqc."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"

from os import path

from snakemake.shell import shell


def basename_without_ext(file_path):
    """Returns basename of file path, without the file extension."""

    base = path.basename(file_path)

    split_ind = 2 if base.endswith(".gz") else 1
    base = ".".join(base.split(".")[:-split_ind])

    return base


# Run fastqc.
output_dir = path.dirname(snakemake.output.html)

shell("fastqc {snakemake.params} --quiet "
      "--outdir {output_dir} {snakemake.input[0]}")

# Move outputs into proper position.
output_base = basename_without_ext(snakemake.input[0])
html_path = path.join(output_dir, output_base + "_fastqc.html")
zip_path = path.join(output_dir, output_base + "_fastqc.zip")

if snakemake.output.html != html_path:
    shell("mv {html_path} {snakemake.output.html}")

if snakemake.output.zip != zip_path:
    shell("mv {zip_path} {snakemake.output.zip}")