__author__ = "Michael Hall"
__copyright__ = "Copyright 2020, Michael Hall"
__email__ = "michael@mbh.sh"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

bases = snakemake.params.get("bases")
if bases:
    extra += f" --bases {bases}"
else:
    covg = snakemake.params.get("coverage")
    gsize = snakemake.params.get("genome_size")
    if covg is None or gsize is None:
        raise ValueError(
            "If `bases` is not given, then `coverage` and `genome_size` must be"
        )
    extra += f" --genome-size {gsize} --coverage {covg}"

shell(
    "rasusa reads {extra} --output {snakemake.output[0]} --output {snakemake.output[1]} {snakemake.input} {log}"
)
