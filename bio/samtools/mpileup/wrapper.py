"""Snakemake wrapper for running mpileup."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bam_input = snakemake.input.bam
reference_genome = snakemake.input.reference_genome

extra = snakemake.params.get("extra", "")

if not snakemake.output[0].endswith(".gz"):
    raise Exception(
        'output file will be compressed and therefore filename should end with ".gz"'
    )

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "samtools mpileup "
    "{extra} "
    "-f {reference_genome} "
    "{bam_input}  "
    " | pigz > {snakemake.output} "
    "{log}"
)
