"""Snakemake wrapper for liftoff"""

__author__ = "Tomás Di Domenico"
__copyright__ = "Copyright 2021, Tomás Di Domenico"
__email__ = "tdido@tdido.ar"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

extra = snakemake.params.get("extra", "")

shell(
    "liftoff "  # tool
    "-g {snakemake.input.ann} "  # annotation file to lift over in GFF or GTF format
    "-o {snakemake.output.main} "  # main output
    "-u {snakemake.output.unmapped} "  # unmapped output
    "{extra} "  # optional parameters
    "{snakemake.input.tgt} "  # target fasta genome to lift genes to
    "{snakemake.input.ref} "  # reference fasta genome to lift genes from
    "{log}"  # Logging
)
