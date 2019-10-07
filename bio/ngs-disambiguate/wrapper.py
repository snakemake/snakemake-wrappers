"""Snakemake wrapper for ngs-disambiguate (from Astrazeneca)."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from os import path

from snakemake.shell import shell


# Extract arguments.
prefix = snakemake.params.get("prefix", None)
extra = snakemake.params.get("extra", "")

output_dir = path.dirname(snakemake.output.a_ambiguous)
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

# If prefix is not given, we use the summary path to derive the most
# probable sample name (as the summary path is least likely to contain)
# additional suffixes. This is better than using a random id as prefix,
# the prefix is also used as the sample name in the summary file.
if prefix is None:
    prefix = path.splitext(path.basename(snakemake.output.summary))[0]

# Run command.
shell(
    "ngs_disambiguate"
    " {extra}"
    " -o {output_dir}"
    " -s {prefix}"
    " -a {snakemake.params.algorithm}"
    " {snakemake.input.a}"
    " {snakemake.input.b}"
)

# Move outputs into expected positions.
output_base = path.join(output_dir, prefix)

output_map = {
    output_base + ".ambiguousSpeciesA.bam": snakemake.output.a_ambiguous,
    output_base + ".ambiguousSpeciesB.bam": snakemake.output.b_ambiguous,
    output_base + ".disambiguatedSpeciesA.bam": snakemake.output.a_disambiguated,
    output_base + ".disambiguatedSpeciesB.bam": snakemake.output.b_disambiguated,
    output_base + "_summary.txt": snakemake.output.summary,
}

for src, dest in output_map.items():
    if src != dest:
        shell("mv {src} {dest}")
