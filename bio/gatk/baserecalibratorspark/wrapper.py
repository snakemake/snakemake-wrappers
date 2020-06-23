__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2020, Christopher Schröder"
__email__ = "christopher.schroeder@tu-dortmund.de"
__license__ = "MIT"


from tempfile import TemporaryDirectory
import os

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
spark_runner = snakemake.params.get("spark_runner", "LOCAL")
spark_master = snakemake.params.get(
    "spark_runner", "local[{}]".format(snakemake.threads)
)
spark_extra = snakemake.params.get("spark_extra", "")
java_opts = snakemake.params.get("java_opts", "")

with TemporaryDirectory() as tmpdir:
    recal_table = os.path.join(tmpdir, "recal_table.grp")
    log = snakemake.log_fmt_shell(stdout=True, stderr=True)
    known = snakemake.input.get("known", "")
    if known:
        known = "--known-sites {}".format(known)

    shell(
        "gatk --java-options '{java_opts}' BaseRecalibratorSpark {extra} "
        "-R {snakemake.input.ref} -I {snakemake.input.bam} "
        "-O {recal_table} {known} "
        "-- --spark-runner {spark_runner} --spark-master {spark_master} {spark_extra} "
        "{log}"
    )

    log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
    shell(
        "gatk --java-options '{java_opts}' ApplyBQSR -R {snakemake.input.ref} -I {snakemake.input.bam} "
        "--bqsr-recal-file {recal_table} "
        "-O {snakemake.output.bam} {log}"
    )
