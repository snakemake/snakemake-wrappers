__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

jsd_sample = snakemake.input.get("jsd_sample")
out_counts = snakemake.output.get("counts")
out_metrics = snakemake.output.get("qc_metrics")
param_thr = snakemake.threads

optional_output = ""
threads = ""
jsd = ""

if jsd_sample:
    jsd += " --JSDsample {jsd} ".format(jsd=jsd_sample)

if out_counts:
    optional_output += " --outRawCounts {out_counts} ".format(out_counts=out_counts)

if out_metrics:
    optional_output += " --outQualityMetrics {metrics} ".format(metrics=out_metrics)

if param_thr:
    threads += " --numberOfProcessors {thr} ".format(thr=param_thr)

shell(
    "(plotFingerprint "
    "-b {snakemake.input.bam_files} "
    "-o {snakemake.output.fingerprint} "
    "{optional_output} "
    "{threads} "
    "{jsd} "
    "{snakemake.params}) {log}"
)
