__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


"""Wrapper for delly.

Example:

rule delly:
    input:
        fasta="genome.fasta",
        bams=expand("mapped/{sample}.bam", sample=config["samples"])
    output:
        bam="sv/{type,(DEL|DUP|INV|TRA|INS)}.vcf"
    log:
        "logs/delly/{type}.log"
    threads: 16
    script:
        "ce8c887/bio/delly"
"""


from snakemake.shell import shell


shell(
    "OMP_NUM_THREADS={snakemake.threads} delly -t {snakemake.wildcards.type} "
    "-g {snakemake.input.fasta} {snakemake.input.bams} "
    "> {snakemake.output} 2> {snakemake.log}")
