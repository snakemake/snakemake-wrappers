__author__ = "Ilya Flyamer"
__copyright__ = "Copyright 2022, Ilya Flyamer"
__email__ = "flyamer@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

## Extract arguments
window = " ".format(snakemake.params.get("window", ""))
chunksize = snakemake.params.get("chunksize", 20000000)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


shell(
    "(cooltools insulation"
    " {snakemake.input.cooler}::resolutions/{snakemake.wildcards.resolution} "
    " {window} --chunksize {chunksize} "
    #    " -p {snakemake.threads} "
    " > {snakemake.output}) {log}"
)
