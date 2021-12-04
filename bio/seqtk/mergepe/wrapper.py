"""Snakemake wrapper for interleaving reads from paired FASTA/Q files using seqtk."""

__author__ = "Michael Hall"
__copyright__ = "Copyright 2021, Michael Hall"
__email__ = "michael@mbh.sh"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True, append=False)
compress_lvl = int(snakemake.params.get("compress_lvl", 6))

shell(
    "(seqtk mergepe {snakemake.input} "
    "| pigz -{compress_lvl} -c -p {snakemake.threads}) > {snakemake.output} {log}"
)
