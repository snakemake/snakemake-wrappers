__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2024, Antonie Vietor, Lance Parsons"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

import re

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

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
    "{extra}) {log}"
)
