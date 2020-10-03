__author__ = "Antonie Vietor"
__copyright__ = "Copyright 2020, Antonie Vietor"
__email__ = "antonie.v@gmx.de"
__license__ = "MIT"

from snakemake.shell import shell
import os

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

genome = snakemake.input.get("genome", "")
extra = snakemake.params.get("extra", "")

# optional input files
gtf = snakemake.input.get("gtf", "")
gene = snakemake.input.get("gene", "")
motif_files = snakemake.input.get("motif_files", "")
filter_motiv = snakemake.input.get("filter_motiv", "")
center = snakemake.input.get("center", "")
nearest_peak = snakemake.input.get("nearest_peak", "")
tag = snakemake.input.get("tag", "")
vcf = snakemake.input.get("vcf", "")
bed_graph = snakemake.input.get("bed_graph", "")
wig = snakemake.input.get("wig", "")
map = snakemake.input.get("map", "")
cmp_genome = snakemake.input.get("cmp_genome", "")
cmp_Liftover = snakemake.input.get("cmp_Liftover", "")
adv_ann = snakemake.input.get("advanced_annotation", "")

# optional output files
matrix = snakemake.output.get("matrix", "")
mfasta = snakemake.output.get("mfasta", "")
mbed = snakemake.output.get("mbed", "")
mlogic = snakemake.output.get("mlogic", "")
gene_ontology_dir = snakemake.output.get("gene_ontology_dir", "")
genome_ontology_dir = snakemake.output.get("genome_ontology_dir", "")

if genome == "":
    genome = "none"

# optional files
opt_files = {
    gtf: "-gtf",
    gene: "-gene",
    motif_files: "-m",
    filter_motiv: "-fm",
    center: "-center",
    nearest_peak: "-p",
    tag: "-d",
    vcf: "-vcf",
    bed_graph: "-bedGraph",
    wig: "-wig",
    map: "-map",
    cmp_genome: "-cmpGenome",
    cmp_Liftover: "-cmpLiftover",
    adv_ann: "-ann",
    mfasta: "-mfasta",
    mbed: "-mbed",
    mlogic: "-mlogic",
}

requires_motives = False
for i in opt_files:
    if i and not i == "":
        extra += " {flag} {file}".format(flag=opt_files[i], file=i)
        if not requires_motives:
            if i == mfasta or i == mbed or i == mlogic:
                requires_motives = True

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
