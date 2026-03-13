__author__ = "Jorge Alvarez-Jarreta"
__copyright__ = "Copyright 2026, Jorge Alvarez-Jarreta"
__mail__ = "jalvarez@ebi.ac.uk"
__license__ = "Apache License 2.0"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

shell("gt gff3validator {extra} {snakemake.input.gff3} {log}")
shell("cp {snakemake.input.gff3} {snakemake.output.gff3}")
