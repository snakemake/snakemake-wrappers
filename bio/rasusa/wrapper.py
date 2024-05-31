__author__ = "Michael Hall"
__copyright__ = "Copyright 2020, Michael Hall"
__email__ = "michael@mbh.sh"
__license__ = "MIT"


from snakemake.shell import shell


extra = snakemake.params.get("extra", "")

bases = snakemake.params.get("bases")
if bases:
    extra += f" -b {bases}"
else:
    covg = snakemake.params.get("coverage")
    gsize = snakemake.params.get("genome_size")
    if covg is None or gsize is None:
        raise ValueError(
            "If `bases` is not given, then `coverage` and `genome_size` must be"
        )
    extra += f" -g {gsize} -c {covg}"

shell("rasusa reads -i {snakemake.input} {extra} -o {snakemake.output} 2> {snakemake.log}")

