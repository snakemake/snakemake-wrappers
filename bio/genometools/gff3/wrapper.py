__author__ = "Jorge Alvarez-Jarreta"
__copyright__ = "Copyright 2026, Jorge Alvarez-Jarreta"
__mail__ = "jalvarez@ebi.ac.uk"
__license__ = "Apache License 2.0"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

shell("gt gff3 {extra} -o {snakemake.output[0]} {snakemake.input[0]} {log}")
