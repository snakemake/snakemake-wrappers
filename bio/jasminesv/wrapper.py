import tempfile
from contextlib import ExitStack
from typing import Sequence, Iterable

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

vcfs = snakemake.input.vcfs
if isinstance(vcfs, str) or len(vcfs) < 2:
    raise ValueError(
        "Jasmine requires at least 2 VCF files to merge. Input 'vcfs' must be a list."
    )

bams = snakemake.input.get("bams")
if bams:
    if isinstance(vcfs, str) or len(bams) != len(vcfs):
        raise ValueError(
            "The number of input BAM files must match the number of input VCF files."
        )

fasta = snakemake.input.get("fasta")
if fasta:
    extra += f" genome_file={fasta}"

chr_norm_file = snakemake.input.get("chr_norm_file")
if chr_norm_file:
    extra += f" chr_norm_file={chr_norm_file}"

sample_dists = snakemake.params.get("sample_dists")
if sample_dists:
    if not isinstance(sample_dists, (Sequence, Iterable)) or len(sample_dists) != len(
        vcfs
    ):
        raise ValueError(
            "The parameter 'sample_dists' must be a list with the same length as the input VCF files."
        )

out_dir = snakemake.output.get("out_dir")
if out_dir:
    extra += f" out_dir={out_dir}"


with ExitStack() as stack:
    vcf_list_file = stack.enter_context(tempfile.NamedTemporaryFile("w", delete=True))
    for vcf in vcfs:
        vcf_list_file.write(f"{vcf}\n")
    vcf_list_file.flush()

    if bams:
        bam_list_file = stack.enter_context(
            tempfile.NamedTemporaryFile("w", delete=True)
        )
        for bam in bams:
            bam_list_file.write(f"{bam}\n")
        bam_list_file.flush()
        extra += f" bam_list={bam_list_file.name}"

    if sample_dists:
        dists_list_file = stack.enter_context(
            tempfile.NamedTemporaryFile("w", delete=True)
        )
        for dist in sample_dists:
            dists_list_file.write(f"{dist}\n")
        dists_list_file.flush()
        extra += f" sample_dists={dists_list_file.name}"

    shell(
        "jasmine "
        "file_list={vcf_list_file.name} "
        "out_file={snakemake.output.vcf} "
        "threads={snakemake.threads} "
        "{extra} "
        "{log}"
    )
