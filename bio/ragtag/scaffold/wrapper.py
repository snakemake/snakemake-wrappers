"""Snakemake wrapper for ragtag-scaffold."""

__author__ = "Curro Campuzano Jiménez"
__copyright__ = "Copyright 2023, Curro Campuzano Jiménez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import os.path


log = snakemake.log_fmt_shell()

# Check that two input files were supplied
n = len(snakemake.input)
assert n == 2, "Input must contain 2 files. Given: %r." % n
query = snakemake.input.query
reference = snakemake.input.reference

# Check that four output files were supplied
m = len(snakemake.output)
assert m >= 3, (
    "Output must contain three files (FASTA, AGP file and summary). Given: %r." % m
)

# Check that all output files are in the same directory
out_dir = os.path.dirname(snakemake.output[0])
for file_path in snakemake.output[1:]:
    assert out_dir == os.path.dirname(file_path), (
        "ragtag can only output files to a single directory."
        " Please indicate only one directory for the output files."
    )

shell(
    "ragtag.py scaffold"
    " {snakemake.input.reference}"
    " {snakemake.input.query}"
    " {snakemake.params.extra}"
    " -o {out_dir}"
    " {log}"
)
