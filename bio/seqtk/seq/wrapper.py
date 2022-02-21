"""Snakemake wrapper seqtk seq subcommand"""

__author__ = "William Rowell"
__copyright__ = "Copyright 2020, William Rowell"
__email__ = "wrowell@pacb.com"
__license__ = "MIT"


from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell("(seqtk seq {extra} {snakemake.input} > {snakemake.output}) {log}")
