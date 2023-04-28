__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell
from tempfile import TemporaryDirectory

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

blacklist = snakemake.input.get("blacklist", "")
if blacklist:
    blacklist = f"--blackListFileName {blacklist}"

out_tab = snakemake.output.get("matrix_tab")
out_bed = snakemake.output.get("matrix_bed")

optional_output = ""

if out_tab:
    optional_output += " --outFileNameMatrix {out_tab} ".format(out_tab=out_tab)

if out_bed:
    optional_output += " --outFileSortedRegions {out_bed} ".format(out_bed=out_bed)


with TemporaryDirectory() as tempdir:
    temp = ""
    if "deepBlueURL" in snakemake.params.extra:
        temp = f"--deepBlueTempDir {tempdir}"

    shell(
        "computeMatrix "
        "{snakemake.params.command} "
        "{snakemake.params.extra} "
        "--numberOfProcessors {snakemake.threads} "
        "-R {snakemake.input.bed} "
        "-S {snakemake.input.bigwig} "
        "-o {snakemake.output.matrix_gz} "
        "{blacklist} {optional_output} {temp} {log}"
    )
