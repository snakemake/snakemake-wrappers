__author__ = "Johannes Köster"
__copyright__ = "Copyright 2018, Johannes Köster"
__email__ = "johannes.koester@protonmail.com"
__license__ = "MIT"


from tempfile import TemporaryDirectory
import os

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

with TemporaryDirectory() as tmpdir:
    recal_table = os.path.join(tmpdir, "recal_table.grp")
    log = snakemake.log_fmt_shell(stdout=True, stderr=True)
    shell("gatk BaseRecalibrator {extra} "
          "-R {snakemake.input.ref} -I {snakemake.input.bam} "
          "-O {recal_table} --known-sites {snakemake.input.known} {log}")

    log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
    shell("gatk ApplyBQSR -R {snakemake.input.ref} -I {snakemake.input.bam} "
          "--bqsr-recal-file {recal_table} "
          "-O {snakemake.output.bam} {log}")
