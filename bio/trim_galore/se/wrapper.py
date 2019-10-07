"""Snakemake wrapper for trimming unpaired reads using trim_galore."""

__author__ = "Kerrin Mendler"
__copyright__ = "Copyright 2018, Kerrin Mendler"
__email__ = "mendlerke@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import os.path


log = snakemake.log_fmt_shell()

# Don't run with `--fastqc` flag
if "--fastqc" in snakemake.params.get("extra", ""):
    raise ValueError(
        "The trim_galore Snakemake wrapper cannot "
        "be run with the `--fastqc` flag. Please "
        "remove the flag from extra params. "
        "You can use the fastqc Snakemake wrapper on "
        "the input and output files instead."
    )

# Check that two output files were supplied
m = len(snakemake.output)
assert m == 2, "Output must contain 2 files. Given: %r." % m

# Check that all output files are in the same directory
out_dir = os.path.dirname(snakemake.output[0])
for file_path in snakemake.output[1:]:
    assert out_dir == os.path.dirname(file_path), (
        "trim_galore can only output files to a single directory."
        " Please indicate only one directory for the output files."
    )

shell(
    "(trim_galore"
    " {snakemake.params.extra}"
    " -o {out_dir}"
    " {snakemake.input})"
    " {log}"
)
