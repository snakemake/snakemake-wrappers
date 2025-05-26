__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
genome = snakemake.input.get("genome", "")
faidx = snakemake.input.get("faidx", "")

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

compress = "| bgzip" if snakemake.output[0].endswith(".gz") else ""

if genome:
    extra += " -g {}".format(genome)
elif faidx:
    extra += " -faidx {}".format(faidx)

shell(
    "(bedtools sort"
    " {extra}"
    " -i {snakemake.input.in_file}"
    " {compress}"
    " > {snakemake.output[0]})"
    " {log}"
)
