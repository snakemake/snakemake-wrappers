__author__ = "Felix Mölder"
__copyright__ = "Copyright 2022, Felix Mölder"
__email__ = "felix.moelder@uk-essen.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")

shell(
    "rbt collapse-reads-to-fragments bam {extra} {snakemake.input[0]} {snakemake.output} {log}"
)
