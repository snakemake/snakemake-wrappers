"""Snakemake wrapper for ragtag-merge."""

__author__ = "Curro Campuzano Jiménez"
__copyright__ = "Copyright 2023, Curro Campuzano Jiménez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import tempfile


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

fasta_file = snakemake.input.get("fasta")
# Check fasta_file is no
assert fasta_file, "Input must contain only one fasta file."

agp_files = snakemake.input.get("agps")

assert len(agp_files) >= 2, "Input must contain at least 2 agp files. Given: %r." % len(
    agp_files
)

bam_file = snakemake.input.get("bam")

# Add Hi-C BAM file to params if present
if bam_file:
    extra += f" -b {bam_file}"

# Raise warning if links file is expected but no Hi-C BAM file is given
if snakemake.output.get("links") and not bam_file:
    raise "Links file is present but no Hi-C BAM file is given."

# Check that all keys in snakemake output are valid are either agp, fasta or links
assert snakemake.output.keys(), "Output must contain at least one named file."
valid_keys = ["agp", "fasta", "links"]
for key in snakemake.output.keys():
    assert (
        key in valid_keys
    ), "Invalid key in output. Valid keys are: %r. Given: %r." % (valid_keys, key)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "ragtag.py merge"
        " {fasta_file}"
        " {agp_files}"
        " {extra}"
        " -o {tmpdir}"
        " {log}"
    )
    for key in valid_keys:
        outfile = snakemake.output.get(key)
        if outfile:
            shell("mv {tmpdir}/ragtag.merge.{key} {outfile}")
