# coding: utf-8

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2024, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory
from os.path import commonprefix

# Optional parameters
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
extra = snakemake.params.get("extra", "")

index = commonprefix(snakemake.input.bowtie).rstrip(".")

with TemporaryDirectory() as tempdir:
    shell(
        "makesnvpattern.pl "
        "{snakemake.input.bed} "
        "{snakemake.input.fasta} "
        "{index} {tempdir} snake_out {log}"
    )

    # Ensure user can name each file according to their need
    output_mapping = {
        "bowtie": f"{tempdir}/snake_out.bowtieout",
        "fasta": f"{tempdir}/snake_out.fasta",
        "ntm": f"{tempdir}/snake_out.ntm",
        "pattern": f"{tempdir}/snake_out.pt",
        "pattern_text": f"{tempdir}/snake_out.pt-txt",
        "pattern_sorted": f"{tempdir}/snake_out.pt-txt.sorted",
        "text": f"{tempdir}/snake_out.txt",
        "uniq": f"{tempdir}/snake_out.uniq.txt",
        "txt_sorted": f"{tempdir}/snake_out.uniq.txt.sorted",
    }

    for output_key, temp_file in output_mapping.items():
        output_path = snakemake.output.get(output_key)
        if output_path:
            shell("mv --verbose {temp_file:q} {output_path:q} {log}")
