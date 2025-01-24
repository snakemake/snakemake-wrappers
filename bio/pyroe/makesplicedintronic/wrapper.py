__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"


from tempfile import TemporaryDirectory
from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
extra = snakemake.params.get("extra", "")

# pyroe uses the flank-length value to name its output files
# in the result directory. We need this value to acquired output
# files and let snakemake-wrapper choose its output file names.
read_length = snakemake.params.get("read_length", 101)
flank_trim_length = snakemake.params.get("flank_trim_length", 5)
flank_length = read_length - flank_trim_length

spliced = snakemake.input.get("spliced", "")
if spliced:
    spliced = "--extra-spliced " + spliced


unspliced = snakemake.input.get("unspliced", "")
if unspliced:
    unspliced = "--extra-unspliced " + unspliced


with TemporaryDirectory() as tempdir:
    shell(
        "pyroe make-spliced+intronic "
        "{extra} {spliced} "
        "{unspliced} "
        "{snakemake.input.fasta} "
        "{snakemake.input.gtf} "
        "{read_length} "
        "{tempdir} "
        "{log}"
    )

    if snakemake.output.get("fasta", False):
        shell(
            "mv --verbose "
            "{tempdir}/splici_fl{flank_length}.fa "
            "{snakemake.output.fasta} {log}"
        )

    if snakemake.output.get("gene_id_to_name", False):
        shell(
            "mv --verbose "
            "{tempdir}/gene_id_to_name.tsv "
            "{snakemake.output.gene_id_to_name} {log}"
        )

    if snakemake.output.get("t2g", False):
        shell(
            "mv --verbose "
            "{tempdir}/splici_fl{flank_length}_t2g_3col.tsv "
            "{snakemake.output.t2g} {log} "
        )
