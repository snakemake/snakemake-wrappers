__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2022, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"


from snakemake.shell import shell

# Formats the log redrection string
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

# Executed shell command
shell(
    "(genefuse "
    "-r {snakemake.input.reference} "
    "-t {snakemake.threads} "
    "-f {snakemake.input.config} "
    "-1 {snakemake.input.fastq1} "
    "-2 {snakemake.input.fastq2} "
    "-h {snakemake.output.html} "
    "{extra} > "
    "{snakemake.output.fusions}) "
    "{log}"
)
