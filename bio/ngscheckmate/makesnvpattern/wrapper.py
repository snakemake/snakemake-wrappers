# coding: utf-8

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2024, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory
from os.path import commonprefix

log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)

index = commonprefix(snakemake.input.index).rstrip(".")

with TemporaryDirectory() as tempdir:
    shell(
        "makesnvpattern.pl "
        "{snakemake.input.bed} "
        "{snakemake.input.fasta} "
        "{index} {tempdir} snake_out {log}"
    )

    # Ensure user can name each file according to their need
    output_mapping = {
        "fasta": f"{tempdir}/snake_out.fasta",
        "pattern": f"{tempdir}/snake_out.pt",
        "txt_uncompressed": f"{tempdir}/snake_out.uniq.txt.sorted",
    }

    for output_key, temp_file in output_mapping.items():
        output_path = snakemake.output.get(output_key)
        if output_path:
            shell("mv --verbose {temp_file:q} {output_path:q} {log}")
