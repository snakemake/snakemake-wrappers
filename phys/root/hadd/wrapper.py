__author__ = "Jamie Gooding"
__copyright__ = "Copyright 2024, Jamie Gooding"
__email__ = "jamie.gooding@cern.ch"
__license__ = "MIT"


from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell()

shell("hadd -j {snakemake.threads} {extra} {snakemake.output} {snakemake.input} {log}")
