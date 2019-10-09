__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2019, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"


from os import path

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

master_file = snakemake.input.master_file
in_sam_file = snakemake.input.sam
out_sam_file = snakemake.output.sam

# Check inputs/arguments.
if not isinstance(master_file, str):
    raise ValueError("master_file, path to the master file")

if not isinstance(in_sam_file, str):
    raise ValueError("sam, path to the input sam file")

if not isinstance(out_sam_file, str):
    raise ValueError("sam, path to the output sam file")

shell(
    "primerclip"
    " {master_file}"
    " {in_sam_file}"
    " {out_sam_file}"
    " {log}")
