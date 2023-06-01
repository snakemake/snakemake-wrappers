"""Snakemake wrapper for ragtag-correction."""

__author__ = "Curro Campuzano Jiménez"
__copyright__ = "Copyright 2023, Curro Campuzano Jiménez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import tempfile

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

# Check that two input files were supplied
n = len(snakemake.input)
assert n == 2, "Input must contain 2 files. Given: %r." % n

assert snakemake.output.keys(), "Output must contain at least one named file."

valid_keys = ["agp", "fasta"]
for key in snakemake.output.keys():
    assert (
        key in valid_keys
    ), "Invalid key in output. Valid keys are: %r. Given: %r." % (valid_keys, key)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "ragtag.py correct"
        " {snakemake.input.ref}"
        " {snakemake.input.query}"
        " {extra}"
        " -o {tmpdir} -t {snakemake.threads}"
        " {log}"
    )

    for key in valid_keys:
        outfile = snakemake.output.get(key)
        if outfile:
            shell("mv {tmpdir}/ragtag.correct.{key} {outfile}")
