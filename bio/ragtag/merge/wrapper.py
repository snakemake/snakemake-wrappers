"""Snakemake wrapper for ragtag-merge."""

__author__ = "Curro Campuzano Jiménez"
__copyright__ = "Copyright 2023, Curro Campuzano Jiménez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import tempfile


log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Check that two input files were supplied
n = len(snakemake.input)
assert n >= 2, "Input must contain at least 2 files. Given: %r." % n

# Check that all keys in snakemake output are valid are either agp, fasta or links
assert snakemake.output.keys(), (
    "Output must contain at least one named file. Given: %r." % n
)

valid_keys = ["agp", "fasta", "links"]
for key in snakemake.output.keys():
    assert (
        key in valid_keys
    ), "Invalid key in output. Valid keys are: %r. Given: %r." % (valid_keys, key)
with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "ragtag.py merge"
        " {snakemake.input}"
        " {snakemake.params.extra}"
        " -o {tmpdir}"
        " {log}"
    )
    for key in valid_keys:
        outfile = snakemake.output.get(key)
        if outfile:
            shell("mv {tmpdir}/ragtag.merge.{key} {outfile}")
