__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


from os import path

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

master_file = snakemake.input.master_file
in_alignment_file = snakemake.input.alignment_file
out_alignment_file = snakemake.output.alignment_file

# Check inputs/arguments.
if not isinstance(master_file, str):
    raise ValueError("master_file, path to the master file")

if not isinstance(in_alignment_file, str):
    raise ValueError("in_alignment_file, path to the input alignment file")

if not isinstance(out_alignment_file, str):
    raise ValueError("out_alignment_file, path to the output file")

samtools_input_command="samtools view -h " + in_alignment_file

shell("{samtools_input_command} |"
    " primerclip"
    " {master_file}"
    " /dev/stdin"
    " {out_alignment_file}"
    " {log}")
