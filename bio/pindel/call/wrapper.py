__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

include_bed = snakemake.input.get("include_bed", None)
exclude_bed = snakemake.input.get("exclude_bed", None)

if include_bed is not None and exclude_bed is not None:
    raise Exception("supply either include_bed or exclude_bed, not both")

include_arg = ""
if include_bed is not None:
    include_arg = "-j {}".format(include_bed)

exclude_arg = ""
if exclude_bed is not None:
    exclude_arg = "-J {}".format(exclude_bed)


shell(
    "pindel "
    "-T {snakemake.threads} "
    "{extra} "
    "{include_arg} "
    "{exclude_arg} "
    "-i {snakemake.input.config} "
    "-f {snakemake.input.ref} "
    "-o {snakemake.params.prefix} {log}"
)
