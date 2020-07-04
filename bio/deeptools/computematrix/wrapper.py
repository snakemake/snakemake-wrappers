__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bed_files = snakemake.input.get("bed")
bigwig_files = snakemake.input.get("bigwig")
out_tab = snakemake.output.get("matrix_tab")
out_bed = snakemake.output.get("matrix_bed")

input_files = "-R "
for bed in bed_files:
    input_files = input_files + bed + " "

input_files = input_files + "-S "
for bigwig in bigwig_files:
    input_files = input_files + bigwig + " "

output_files = "-o " + snakemake.output.get("matrix_gz")

if out_tab and out_tab is not None:
    output_files = output_files + " --outFileNameMatrix " + out_tab + " "

if out_bed and out_bed is not None:
    output_files = output_files + " --outFileSortedRegions " + out_bed + " "

shell(
    "(computeMatrix "
    "{snakemake.params.command} "
    "{snakemake.params.extra} "
    "{input_files} "
    "{output_files}) {log}"
)
