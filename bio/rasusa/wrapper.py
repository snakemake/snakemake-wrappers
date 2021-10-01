__author__ = "Michael Hall"
__copyright__ = "Copyright 2020, Michael Hall"
__email__ = "michael@mbh.sh"
__license__ = "MIT"


from snakemake.shell import shell


options = snakemake.params.get("options", "")

bases = snakemake.params.get("bases")
if bases is not None:
    options += " -b {}".format(bases)
else:
    covg = snakemake.params.get("coverage")
    gsize = snakemake.params.get("genome_size")
    if covg is None or gsize is None:
        raise ValueError(
            "If `bases` is not given, then `coverage` and `genome_size` must be"
        )
    options += " -g {gsize} -c {covg}".format(gsize=gsize, covg=covg)

shell("rasusa {options} -i {snakemake.input} -o {snakemake.output} 2> {snakemake.log}")
