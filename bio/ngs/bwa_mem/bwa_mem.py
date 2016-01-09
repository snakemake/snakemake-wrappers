__author__ = "Johannes Köster"
__copyright__ = "Copyright 2015, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


"""Wrapper for bwa mem.

Example:

rule bwa_mem:
    input:
        fasta="genome.fasta",
        fastq=["reads/{sample}.fastq.gz", "reads/{sample}.fastq.gz"]
    output:
        bam="mapped/{sample}.bam"
    log:
        "logs/bwa_mem/{sample}.log"
    threads: 8
    script:
        "wrappers/bio/ngs/bwa_mem.py"
"""


from snakemake.shell import shell


shell(
    "bwa mem {snakemake.threads} {snakemake.input.fasta} "
    "{snakemake.input.fastq} | samtools view -Sbh - > "
    "{snakemake.output.bam} 2> {snakemake.log}")
