__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


shell(
    "bwa mem {snakemake.threads} {snakemake.input.fasta} "
    "{snakemake.input.fastq} | samtools view -Sbh - > "
    "{snakemake.output.bam} 2> {snakemake.log}")
