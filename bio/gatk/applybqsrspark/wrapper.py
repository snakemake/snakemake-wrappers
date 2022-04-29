__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"

import tempfile
import random
from pathlib import Path

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
spark_runner = snakemake.params.get("spark_runner", "LOCAL")
spark_master = snakemake.params.get(
    "spark_master", "local[{}]".format(snakemake.threads)
)
spark_extra = snakemake.params.get("spark_extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

with tempfile.TemporaryDirectory() as tmpdir:
    # This folder must not exist; it is created by GATK
    tmpdir_shards = Path(tmpdir) / "shards_{:06d}".format(random.randrange(10**6))

    shell(
        "gatk --java-options '{java_opts}' ApplyBQSRSpark"
        " --input {snakemake.input.bam}"
        " --bqsr-recal-file {snakemake.input.recal_table}"
        " --reference {snakemake.input.ref}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output-shard-tmp-dir {tmpdir_shards}"
        " --output {snakemake.output.bam}"
        " -- --spark-runner {spark_runner} --spark-master {spark_master} {spark_extra}"
        " {log}"
    )
