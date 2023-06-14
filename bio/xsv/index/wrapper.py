__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

if str(snakemake.input[0]).endswith("tsv"):
    extra = "--delimiter $'\t'"


shell(
    "xsv index "
    "{extra} "
    " --output {snakemake.output} "
    "{snakemake.input[0]} "
    "{log} "
)
