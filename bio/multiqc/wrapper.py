"""Snakemake wrapper for trimming paired-end reads using cutadapt."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from os import path

from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
# Set this to False if multiqc should use the actual input directly
# instead of parsing the folders where the provided files are located
convert_file_input_to_dirs = snakemake.params.get("use_files_as_input", True)

if convert_file_input_to_dirs:
    input_data = set(path.dirname(fp) for fp in snakemake.input)
else:
    input_data = set(snakemake.input)

output_dir = path.dirname(snakemake.output[0])
output_name = path.basename(snakemake.output[0])
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "multiqc"
    " {extra}"
    " --force"
    " -o {output_dir}"
    " -n {output_name}"
    " {input_data}"
    " {log}"
)
