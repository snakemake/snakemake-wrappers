__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

bed = snakemake.input.get("bed", "")
if bed:
    bed = " --BED " + bed

raw_counts = snakemake.output.get("raw_counts", "")
if raw_counts:
    raw_counts = " --outRawCounts " + raw_counts

metrics = snakemake.output.get("metrics", "")
if metrics:
    metrics = " --outCoverageMetrics " + metrics


blacklist = snakemake.input.get("blacklist", "")
if blacklist:
    blacklist = " --blackListFileName " + blacklist


out_tab = snakemake.output.get("matrix_tab")
out_bed = snakemake.output.get("matrix_bed")

optional_output = ""

if out_tab:
    optional_output += " --outFileNameMatrix {out_tab} ".format(out_tab=out_tab)

if out_bed:
    optional_output += " --outFileSortedRegions {out_bed} ".format(out_bed=out_bed)

shell(
    "plotCoverage"
    "{snakemake.params.extra} "
    "{bed} {raw_counts} {metrics} "
    "{blacklist} "
    "--numberOfProcessors {snakemake.threads} "
    "--bamfiles {snakemake.input.bams} "
    " {log}"
)
