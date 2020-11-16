__author__ = "Michael Hall"
__copyright__ = "Copyright 2020, Michael Hall"
__email__ = "michael@mbh.sh"
__license__ = "MIT"


from snakemake.shell import shell


options = snakemake.params.get("options", "")


shell(
    "rasusa {options} -i {snakemake.input} -o {snakemake.output} "
    "-c {snakemake.params.coverage} -g {snakemake.params.genome_size} "
    "2> {snakemake.log}"
)
