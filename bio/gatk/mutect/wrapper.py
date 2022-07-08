"""Snakemake wrapper for GATK4 Mutect2"""

__author__ = "Thibault Dayris"
__copyright__ = "Copyright 2019, Dayris Thibault"
__email__ = "thibault.dayris@gustaveroussy.fr"
__license__ = "MIT"

import tempfile
from snakemake.shell import shell
from snakemake.utils import makedirs
from snakemake_wrapper_utils.java import get_java_opts

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bam_output = ""
if "bam" in snakemake.output.keys():
    bam_output = "--bam-output {}".format(snakemake.output["bam"])


germline_resource = ""
if "germline" in snakemake.input.keys():
    germline_resource = "--germline-resource {}".format(
        snakemake.input["germline"]
    )

intervals = ""
if "intervals" in snakemake.input.keys():
    intervals = "--intervals {}".format(snakemake.input["intervals"])


f1r2 = ""
if "f1r2" in snakemake.output.keys():
    f1r2 = "--f1r2-tar-gz {}".format(snakemake.output["f1r2"])

pon = ""
if "pon" in snakemake.input.keys():
    pon = "--panel-of-normals {}".format(snakemake.input["pon"])

extra = snakemake.params.get("extra", "")
java_opts = get_java_opts(snakemake)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "gatk --java-options '{java_opts}' Mutect2"  # Tool and its subprocess
        " --native-pair-hmm-threads {snakemake.threads}"
        " --input {snakemake.input.map}"  # Path to input mapping file
        " --reference {snakemake.input.fasta}"  # Path to reference fasta file
        " {f1r2}"  # Optional path to output f1r2 count file
        " {germline_resource}"  # Optional path to optional germline resource VCF
        " {intervals}"  # Optional path to optional bed intervals
        " {pon} "  # Optional path to panel of normals
        " {extra}"  # Extra parameters
        " --tmp-dir {tmpdir}"
        " --output {snakemake.output.vcf}"  # Path to output vcf file
        " {bam_output}"  # Path to output bam file, optional
        " {log}"  # Logging behaviour
    )
