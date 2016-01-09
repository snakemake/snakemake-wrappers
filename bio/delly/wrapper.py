__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


shell(
    "OMP_NUM_THREADS={snakemake.threads} delly -t {snakemake.wildcards.type} "
    "-g {snakemake.input.fasta} {snakemake.input.bams} "
    "> {snakemake.output} 2> {snakemake.log}")
