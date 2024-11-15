__author__ = "Felix Mölder"
__copyright__ = "Copyright 2024, Felix Mölder"
__email__ = "felix.moelder@uk-essen.de"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

# Extract arguments.
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

prefix_path = path.commonprefix(snakemake.output).rstrip(".")
vcf_cmd = f"-v {snakemake.input.vcf}" if snakemake.input.get("vcf") else ""


def contains_ext(extensions):
    return all(any(out_file.endswith(ext) for out_file in snakemake.output) for ext in extensions)


if any(lambda x: "giraffe" in x, snakemake.output):
    workflow_cmd = "giraffe"
elif contains_ext([".xg", ".gcsa.lcp", ".gcsa"]):
    workflow_cmd = "map"
else:
    raise ValueError("Output files do not match any supported indexing workflows. Currently only map and giraffe are supported.")

shell(
    "(vg autoindex"
    " -w {workflow_cmd}"
    " -p {prefix_path}"
    " -r {snakemake.input.ref}"
    " {vcf_cmd}"
    " -t {snakemake.threads}"
    " {extra}) {log}"
)