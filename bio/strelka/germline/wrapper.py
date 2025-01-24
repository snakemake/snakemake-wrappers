__author__ = "Jan Forster, Christopher Schröder"
__copyright__ = "Copyright 2019, Jan Forster"
__email__ = "jan.forster@uk-essen.de"
__license__ = "MIT"

import tempfile
import glob

from pathlib import Path
from snakemake.shell import shell

config_extra = snakemake.params.get("config_extra", "")
run_extra = snakemake.params.get("run_extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bam = snakemake.input.get("bam")  # input bam file, required
assert bam is not None, "input-> bam is a required input parameter"
if isinstance(bam, str):
    bam = [bam]

if snakemake.output.get("sample_genomes"):
    assert len(bam) == len(
        snakemake.output.get("sample_genomes")
    ), "number of input bams and sample_genomes must be equal "

if snakemake.output.get("sample_genomes_indices"):
    assert len(bam) == len(
        snakemake.output.get("sample_genomes_indices")
    ), "number of input bams and sample_genomes_indices must be equal "

bam_input = " ".join(f"--bam {b}" for b in bam)

with tempfile.TemporaryDirectory() as tmpdir:
    shell(
        "(configureStrelkaGermlineWorkflow.py "  # configure the strelka run
        "{bam_input} "  # input bam
        "--referenceFasta {snakemake.input.fasta} "  # reference genome
        "--runDir {tmpdir} "  # output directory
        "{config_extra} "  # additional parameters for the configuration
        "&& {tmpdir}/runWorkflow.py "  # run the strelka workflow
        "-m local "  # run in local mode
        "-j {snakemake.threads} "  # number of threads
        "{run_extra}) "  # additional parameters for the run
        "{log}"
    )  # logging

    if snakemake.output.get("variants"):
        shell(
            "cat {tmpdir}/results/variants/variants.vcf.gz > {snakemake.output.variants:q}"
        )
    if snakemake.output.get("variants_index"):
        shell(
            "cat {tmpdir}/results/variants/variants.vcf.gz.tbi > {snakemake.output.variants_index:q}"
        )
    if targets := snakemake.output.get("sample_genomes"):
        origins = glob.glob(f"{tmpdir}/results/variants/genome.S*.vcf.gz")
        assert len(origins) == len(targets)
        for origin, target in zip(origins, targets):
            shell(f"cat {origin} > {target}")
    if targets := snakemake.output.get("sample_genomes_indices"):
        origins = glob.glob(f"{tmpdir}/results/variants/genome.S*.vcf.gz.tbi")
        assert len(origins) == len(targets)
        for origin, target in zip(origins, targets):
            shell(f"cat {origin} > {target}")
