__author__ = "Filipe G. Vieira, Christopher Schröder"
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
reference = snakemake.input.get("ref")
embed_ref = snakemake.params.get("embed_ref", False)
exceed_thread_limit = snakemake.params.get("exceed_thread_limit", False)
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

if exceed_thread_limit:
    samtools_threads = snakemake.threads
else:
    samtools_threads = 1

if snakemake.output.bam.endswith(".cram") and embed_ref:
    output = "/dev/stdout --create-output-bam-splitting-index false"
    pipe_cmd = " | samtools view -h -O cram,embed_ref -T {reference} -o {snakemake.output.bam} -@ {samtools_threads} -"
else:
    output = snakemake.output.bam
    pipe_cmd = ""


with tempfile.TemporaryDirectory() as tmpdir:
    # This folder must not exist; it is created by GATK
    tmpdir_shards = Path(tmpdir) / "shards_{:06d}".format(random.randrange(10**6))

    shell(
        "(gatk --java-options '{java_opts}' ApplyBQSRSpark"
        " --input {snakemake.input.bam}"
        " --bqsr-recal-file {snakemake.input.recal_table}"
        " --reference {snakemake.input.ref}"
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output-shard-tmp-dir {tmpdir_shards}"
        " --output {output}"
        " -- --spark-runner {spark_runner} --spark-master {spark_master} {spark_extra}"
        + pipe_cmd
        + ") {log}"
    )
