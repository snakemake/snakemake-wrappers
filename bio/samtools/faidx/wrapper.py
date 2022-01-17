__author__ = "Michael Chambers"
__copyright__ = "Copyright 2019, Michael Chambers"
__email__ = "greenkidneybean@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "samtools faidx {snakemake.params} {snakemake.input[0]} > {snakemake.output[0]} {log}"
)
