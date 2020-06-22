__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

out = str(snakemake.wildcards.path) + str(snakemake.wildcards.sample)

shell(
    "(picard -Xmx{snakemake.resources.mem_gb}g CollectMultipleMetrics "
    "I={snakemake.input.bam} "
    "O=" + out + " "
    "R={snakemake.input.ref} "
    "{snakemake.params}) {log}"
)
