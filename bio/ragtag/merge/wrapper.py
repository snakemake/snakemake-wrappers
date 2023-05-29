"""Snakemake wrapper for ragtag-merge."""

__author__ = "Curro Campuzano Jiménez"
__copyright__ = "Copyright 2023, Curro Campuzano Jiménez"
__email__ = "campuzanocurro@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import tempfile


log = snakemake.log_fmt_shell(stdout=True, stderr=True)

agp_files = [f for f in snakemake.input if f.endswith(".agp")]
assert len(agp_files) >= 2, "Input must contain at least 2 agp files. Given: %r." % len(
    agp_files
)

bam_file = [f for f in snakemake.input if f.endswith(".bam")]
assert (
    len(bam_file) <= 1
), "Input must contain only one Hi-C BAM file, if any. Given: %r." % len(bam_file)

fasta_file = [
    f for f in snakemake.input if not f.endswith(".bam") and not f.endswith(".agp")
]
assert len(fasta_file) == 1, "Input must contain only one fasta file. Given: %r." % len(
    fasta_file
)

# Add Hi-C BAM file to params if present
if bam_file:
    snakemake.params.extra += f" -b {bam_file[0]}"

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
        " {fasta_file[0]}"
        f" {' '.join(agp_files)}"
        " {snakemake.params.extra}"
        " -o {tmpdir}"
        " {log}"
    )
    for key in valid_keys:
        outfile = snakemake.output.get(key)
        if outfile:
            shell("mv {tmpdir}/ragtag.merge.{key} {outfile}")
