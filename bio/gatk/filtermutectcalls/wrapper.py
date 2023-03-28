__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2021, Patrik Smeds"
__email__ = "patrik.smeds@gmail.com"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

log = snakemake.log_fmt_shell(stdout=True, stderr=True)


aln = snakemake.input.get("aln", "")
if aln:
    aln = f"--input {aln}"

contamination = snakemake.input.get("contemination_table", "")
if contamination:
    contamination = f"--contamination-table {contamination}"

segmentation = snakemake.input.get("segmentation", "")
if segmentation:
    segmentation = f"--tumor-segmentation {segmentation}"

f1r2 = snakemake.input.get("f1r2", "")
if f1r2:
    f1r2 = f"--orientation-bias-artifact-priors {f1r2}"

intervals = snakemake.input.get("bed", "")
if intervals:
    intervals = f"--intervals {intervals}"

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' FilterMutectCalls"
        " --variant {snakemake.input.vcf}"
        " --reference {snakemake.input.ref}"
        " {aln}"  # BAM/SAM/CRAM file containing reads
        " {contamination}"  # Tables containing contamination information
        " {segmentation}"  # Tumor segments' minor allele fractions
        " {f1r2}"  # .tar.gz files containing tables of prior artifact
        " {intervals}"  # Genomic intervals over which to operate
        " {extra}"
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output.vcf}"
        " {log}"
    )
