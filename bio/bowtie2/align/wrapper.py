__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

n = len(snakemake.input.sample)
assert (
    n == 1 or n == 2
), "input->sample must have 1 (single-end) or 2 (paired-end) elements."

if n == 1:
    reads = "-U {}".format(*snakemake.input.sample)
else:
    reads = "-1 {} -2 {}".format(*snakemake.input.sample)

shell(
    "(bowtie2 --threads {snakemake.threads} {extra} "
    "-x {snakemake.params.index} {reads} "
    "| samtools view -Sbh -o {snakemake.output[0]} -) {log}"
)
