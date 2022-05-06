__author__ = "Fillipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
spark_runner = snakemake.params.get("spark_runner", "LOCAL")
spark_master = snakemake.params.get(
    "spark_master", "local[{}]".format(snakemake.threads)
)
spark_extra = snakemake.params.get("spark_extra", "")
java_opts = get_java_opts(snakemake)

metrics = snakemake.output.get("metrics", "")
if metrics:
    metrics = f"--metrics-file {metrics}"

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' MarkDuplicatesSpark"
        " --input {snakemake.input}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output.bam}"
        " {metrics}"
        " -- --spark-runner {spark_runner} --spark-master {spark_master} {spark_extra}"
        " {log}"
    )
