__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

include_bed = snakemake.input.get("include_bed", "")
exclude_bed = snakemake.input.get("exclude_bed", "")

if include_bed and exclude_bed:
    raise Exception("supply either include_bed or exclude_bed, not both")

if include_bed:
    include_bed = f"-j {include_bed}"

if exclude_bed:
    exclude_bed = f"-J {exclude_bed}"

output_prefix = snakemake.output[0].rsplit("_", 1)[0]

shell(
    "pindel "
    "-T {snakemake.threads} "
    "{extra} "
    "{include_bed} "
    "{exclude_bed} "
    "-i {snakemake.input.config} "
    "-f {snakemake.input.ref} "
    "-o {output_prefix} {log}"
)
