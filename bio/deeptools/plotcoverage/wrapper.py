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


accepted_extensions = ["eps", "png", "svg", "pdf"]
out_image_extension = str(snakemake.output["plot"]).split(".")[-1]
if out_image_extension not in accepted_extensions:
    raise ValueError(
        "Wrong image format: {ext}, expected: {expected}".format(
            ext=out_image_extension, expected=str(accepted_extensions)
        )
    )


shell(
    "plotCoverage "
    "{extra} {bed} {raw_counts} {metrics} {blacklist} "
    "--numberOfProcessors {snakemake.threads} "
    "--bamfiles {snakemake.input.bams} "
    "--plotFile {snakemake.output.plot} "
    "--plotFileFormat {out_image_extension} "
    " {log}"
)
