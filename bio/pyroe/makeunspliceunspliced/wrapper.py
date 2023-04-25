__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


from tempfile import TemporaryDirectory
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
extra = snakemake.params.get("extra", "")

spliced = snakemake.input.get("spliced", "")
if spliced:
    spliced = "--extra-spliced " + spliced


unspliced = snakemake.input.get("unspliced", "")
if unspliced:
    unspliced = "--extra-unspliced " + unspliced


with TemporaryDirectory() as tempdir:
    shell(
        "pyroe make-spliced+unspliced "
        "{extra} {spliced} "
        "{unspliced} "
        "{snakemake.input.fasta} "
        "{snakemake.input.gtf} "
        "{tempdir} "
        "{log}"
    )

    if snakemake.output.get("fasta", False):
        shell("mv --verbose {tempdir}/spliceu.fa {snakemake.output.fasta} {log}")

    if snakemake.output.get("gene_id_to_name", False):
        shell(
            "mv --verbose "
            "{tempdir}/gene_id_to_name.tsv "
            "{snakemake.output.gene_id_to_name} {log}"
        )

    if snakemake.output.get("t2g_3col", False):
        shell(
            "mv --verbose "
            "{tempdir}/spliceu_t2g_3col.tsv "
            "{snakemake.output.t2g_3col} {log} "
        )

    if snakemake.output.get("t2g", False):
        shell("mv --verbose {tempdir}/spliceu_t2g.tsv {snakemake.output.t2g} {log} ")

    if snakemake.output.get("g2g", False):
        shell("mv --verbose {tempdir}/spliceu_g2g.tsv {snakemake.output.g2g} {log} ")
