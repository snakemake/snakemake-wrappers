__author__ = "Felix Mölder"
__copyright__ = "Copyright 2024, Felix Mölder"
__email__ = "felix.moelder@uk-essen.de"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

# Extract arguments.
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

prefix_path = path.splitext(snakemake.output[0])[0]
vcf_cmd = f"-v {snakemake.input.vcf}" if snakemake.input.get("vcf") else ""
shell(
    "(vg autoindex -w giraffe"
    " -p {prefix_path}"
    " -r {snakemake.input.ref}"
    " {vcf_cmd}"
    " -t {snakemake.threads}"
    " {extra}) {log}"
)