# coding: utf-8

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2026, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from tempfile import TemporaryDirectory
from snakemake.shell import shell
from snakemake_wrapper_utils.snakemake import move_files, is_arg

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

# There is no way to control output file name, which is why we have to move them.
with TemporaryDirectory() as tempdir:
    genome_link = f"{tempdir}/genome.fasta"
    shell(
        "ln -sfrv {snakemake.input} {genome_link} {log} && "
        "minibwa index -t {snakemake.threads} {extra} {genome_link} "
    )

    expected_outfiles = {
        "l2b": f"{genome_link}.l2b",
        "mbw": f"{genome_link}.mbw",
    }
    if is_arg("--meth", extra):
        expected_outfiles["meth_mbw"] = f"{genome_link}.meth.mbw"

    for move_cmd in move_files(snakemake, expected_outfiles):
        shell("{move_cmd} {log}")
