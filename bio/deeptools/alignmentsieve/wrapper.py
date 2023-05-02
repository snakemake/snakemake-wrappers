__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2023, Thibault Dayris"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

from snakemake.shell import shell


log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

blacklist = snakemake.input.get("blacklist", "")
if blacklist:
    extra += f" --blackListFileName {blacklist} "

out_file = snakemake.output[0]
if out_file.endswith(".bed"):
    extra += " --BED "

shell(
    "alignmentSieve "
    "{extra} "
    "--numberOfProcessors {snakemake.threads} "
    "--bam {snakemake.input.aln} "
    "--outFile {out_file} "
    "{log} "
)
