__author__ = "Kim Philipp Jablonski"
__copyright__ = "Copyright 2020, Kim Philipp Jablonski"
__email__ = "kim.philipp.jablonski@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)


shell(
    "diamond blastx"
    " --threads {snakemake.threads}"
    " --db {snakemake.input.fname_db}"
    " --query {snakemake.input.fname_fastq}"
    " --out {snakemake.output.fname}"
    " {extra}"
    " {log}"
)
