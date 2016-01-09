__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


"""Wrapper for bwa mem.

Example:

rule bwa_mem:
    input:
        fasta="genome.fasta",
        fastq=["reads/{sample}.1.fastq.gz", "reads/{sample}.2.fastq.gz"]
    output:
        bam="mapped/{sample}.bam"
    log:
        "logs/bwa_mem/{sample}.log"
    threads: 8
    script:
        "ce8c887/bio/bwa_mem"
"""


from snakemake.shell import shell


shell(
    "bwa mem {snakemake.threads} {snakemake.input.fasta} "
    "{snakemake.input.fastq} | samtools view -Sbh - > "
    "{snakemake.output.bam} 2> {snakemake.log}")
