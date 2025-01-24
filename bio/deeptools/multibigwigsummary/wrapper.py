# coding: utf-8

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2024, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


from snakemake.shell import shell

# Optional parameters
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

blacklist = snakemake.input.get("blacklist")
if blacklist:
    extra += f" --blackListFileName {blacklist} "

out_raw_counts = snakemake.output.get("counts")
if out_raw_counts:
    extra += f" --outRawCounts {out_raw_counts} "

bed = snakemake.input.get("bed")
subcommand = "bins"
if bed:
    subcommand = "BED-file"
    extra += f" --BED {bed} "


shell(
    "multiBigwigSummary {subcommand} "
    "--bwfiles {snakemake.input.bw} "
    "--outFileName {snakemake.output.npz} "
    "--numberOfProcessors {snakemake.threads} "
    "{extra} {log}"
)
