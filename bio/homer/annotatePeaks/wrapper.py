__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell
import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

genome = snakemake.input.get("genome", "")
extra = snakemake.params.get("extra", "")
motif_files = snakemake.input.get("motif_files", "")
matrix = snakemake.output.get("matrix", "")

if genome == "":
    genome = "none"

# optional files
opt_files = {
    "gtf": "-gtf",
    "gene": "-gene",
    "motif_files": "-m",
    "filter_motiv": "-fm",
    "center": "-center",
    "nearest_peak": "-p",
    "tag": "-d",
    "vcf": "-vcf",
    "bed_graph": "-bedGraph",
    "wig": "-wig",
    "map": "-map",
    "cmp_genome": "-cmpGenome",
    "cmp_Liftover": "-cmpLiftover",
    "advanced_annotation": "-ann",
    "mfasta": "-mfasta",
    "mbed": "-mbed",
    "mlogic": "-mlogic",
}

requires_motives = False
for i in opt_files:
    file = None
    if i == "mfasta" or i == "mbed" or i == "mlogic":
        file = snakemake.output.get(i, "")
        if file:
            requires_motives = True
    else:
        file = snakemake.input.get(i, "")
    if file:
        extra += " {flag} {file}".format(flag=opt_files[i], file=file)

if requires_motives and motif_files == "":
    sys.exit(
        "The optional output files require motif_file(s) as input. For more information please see http://homer.ucsd.edu/homer/ngs/annotation.html."
    )

# optional matrix output files:
if matrix:
    if motif_files == "":
        sys.exit(
            "The matrix output files require motif_file(s) as input. For more information please see http://homer.ucsd.edu/homer/ngs/annotation.html."
        )
    ext = ".count.matrix.txt"
    matrix_out = [i for i in snakemake.output if i.endswith(ext)][0]
    matrix_name = os.path.basename(matrix_out[: -len(ext)])
    extra += " -matrix {}".format(matrix_name)

shell(
    "(annotatePeaks.pl"
    " {snakemake.params.mode}"
    " {snakemake.input.peaks}"
    " {genome}"
    " {extra}"
    " -cpu {snakemake.threads}"
    " > {snakemake.output.annotations})"
    " {log}"
)
