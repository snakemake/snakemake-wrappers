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
    if not "--coverageThresholds" in extra:
        raise ValueError(
            "Coverage metrics without a `--coverageThresholds` in "
            "extra parameters will result in an empty file. Please "
            "provide `--coverageThresholds` or remove "
            "metrics file from expected output files."
        )


blacklist = snakemake.input.get("blacklist", "")
if blacklist:
    blacklist = " --blackListFileName " + blacklist


shell(
    "plotCoverage "
    "{extra} {bed} {raw_counts} {metrics} {blacklist} "
    "--numberOfProcessors {snakemake.threads} "
    "--bamfiles {snakemake.input.bams} "
    "--plotFile {snakemake.output.plot} "
    " {log}"
)
