__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


shell(
    "(samtools mpileup {snakemake.params.mpileup} {snakemake.input.samples} "
    "--fasta-ref {snakemake.input.ref} --BCF --uncompressed | "
    "bcftools call -m {snakemake.params.call} -o {snakemake.output[0]} -v -) 2> {snakemake.log}")
