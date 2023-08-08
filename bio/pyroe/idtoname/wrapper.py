__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
extra = snakemake.params.get("extra", "")

if str(snakemake.input).endswith(("gtf", "gtf.gz")):
    extra += " --format GTF "
elif str(snakemake.input).endswith(("gff", "gff.gz", "gff3", "gff3.gz")):
    extra += " --format GFF3 "

shell("pyroe id-to-name {extra} {snakemake.input} {snakemake.output} {log}")
