__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell
import re

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

jsd_sample = snakemake.input.get("jsd_sample")
out_counts = snakemake.output.get("counts")
out_metrics = snakemake.output.get("qc_metrics")
optional_output = ""
jsd = ""

if jsd_sample:
    jsd += " --JSDsample {jsd} ".format(jsd=jsd_sample)

if out_counts:
    optional_output += " --outRawCounts {out_counts} ".format(out_counts=out_counts)

if out_metrics:
    optional_output += " --outQualityMetrics {metrics} ".format(metrics=out_metrics)

shell(
    "(plotFingerprint "
    "-b {snakemake.input.bam_files} "
    "-o {snakemake.output.fingerprint} "
    "{optional_output} "
    "--numberOfProcessors {snakemake.threads} "
    "{jsd} "
    "{snakemake.params}) {log}"
)
# ToDo: remove the 'NA' string replacement when fixed in deepTools, see:
# https://github.com/deeptools/deepTools/pull/999
regex_passes = 2

with open(out_metrics, "rt") as f:
    metrics = f.read()
    for i in range(regex_passes):
        metrics = re.sub("\tNA(\t|\n)", "\tnan\\1", metrics)

with open(out_metrics, "wt") as f:
    f.write(metrics)
