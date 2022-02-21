"""Snakemake wrapper for running mpileup."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

if not snakemake.output[0].endswith(".gz"):
    raise Exception(
        'output file will be compressed and therefore filename should end with ".gz"'
    )

shell(
    "(samtools mpileup {extra} -f {snakemake.input.reference_genome} {snakemake.input.bam} | pigz > {snakemake.output}) {log}"
)
