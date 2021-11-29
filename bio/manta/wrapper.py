__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"


import math
from snakemake.shell import shell
from pathlib import Path
from tempfile import TemporaryDirectory


extra_cfg = snakemake.params.get("extra_cfg", "")
extra_run = snakemake.params.get("extra_run", "")

bed = snakemake.input.get("bed", "")
if bed:
    bed = f"--regions-file {bed} --regions-overlap 1"

mem_gb = math.ceil(snakemake.resources.get("mem_mb", "") / 1024)
if not mem_gb:
    mem_gb = snakemake.resources.get("mem_gb", "")
if mem_gb:
    mem_gb = f"--memGb {mem_gb}"

log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)


with TemporaryDirectory() as tempdir:
    tempdir = Path(tempdir)
    run_dir = tempdir / "runDir"
    bams = []

    # Symlink BAM/CRAM files to avoid problems with filenames
    for aln, idx in zip(snakemake.input.samples, snakemake.input.idx):
        Path(tempdir / Path(aln).name).symlink_to(aln)
        bams.append(tempdir / Path(aln).name)

        if idx.endswith(".bam.bai") or idx.endswith(".cram.crai"):
            Path(tempdir / Path(idx).name).symlink_to(idx)
        elif idx.endswith(".bai"):
            Path(tempdir / Path(idx).stem + ".bam.bai").symlink_to(idx)
        elif idx.endswith(".crai"):
            Path(tempdir / Path(idx).stem + ".cram.crai").symlink_to(idx)
        else:
            raise ValueError(f"invalid index file name provided: {idx}")

    shell(
        # Configure Manta
        "configManta.py {extra_cfg} {bams} --referenceFasta {snakemake.input.ref} --runDir {run_dir} {log}; "
        # Run Manta
        "python2 {run_dir}/runWorkflow.py {extra_run} --jobs {snakemake.threads} {mem_gb} {log}; "
    )

    # Copy outputs into proper position.
    results_base = run_dir / "results" / "variants"

    def infer_vcf_ext(vcf):
        if vcf.endswith(".vcf.gz"):
            return "z"
        elif vcf.endswith(".bcf"):
            return "b"
        else:
            raise ValueError(
                "invalid VCF extension. Only '.vcf.gz' and '.bcf' are supported."
            )

    # Copy main VCF output
    vcf = snakemake.output.get("vcf", "")
    vcf_path = results_base / "diploidSV.vcf.gz"
    if vcf and vcf != vcf_path:
        vcf_format = infer_vcf_ext(vcf)
        shell(
            "bcftools view --threads {snakemake.threads} {bed} --output-file {vcf:q} --output-type {vcf_format} {vcf_path:q}"
        )

        idx = snakemake.output.get("idx", "")
        idx_path = results_base / "diploidSV.vcf.gz.tbi"
        if idx and idx != idx_path:
            shell(
                "bcftools index --threads {snakemake.threads} --output-file {idx:q} {vcf:q}"
            )

    # Copy candidate small indels VCF
    cand_indel_vcf = snakemake.output.get("cand_indel_vcf", "")
    cand_indel_vcf_path = results_base / "candidateSmallIndels.vcf.gz"
    if cand_indel_vcf and cand_indel_vcf != cand_indel_vcf_path:
        cand_indel_vcf_format = infer_vcf_ext(cand_indel_vcf)
        shell(
            "bcftools view --threads {snakemake.threads} {bed} --output-file {cand_indel_vcf:q} --output-type {cand_indel_vcf_format} {cand_indel_vcf_path:q}"
        )

        cand_indel_idx = snakemake.output.get("cand_indel_idx", "")
        cand_indel_idx_path = results_base / "candidateSmallIndels.vcf.gz.tbi"
        if cand_indel_idx and cand_indel_idx != cand_indel_idx_path:
            shell(
                "bcftools index --threads {snakemake.threads} --output-file {cand_indel_idx:q} {cand_indel_vcf:q}"
            )

    # Copy candidates structural variants VCF
    cand_sv_vcf = snakemake.output.get("cand_sv_vcf", "")
    cand_sv_vcf_path = results_base / "candidateSV.vcf.gz"
    if cand_sv_vcf and cand_sv_vcf != cand_sv_vcf_path:
        cand_sv_vcf_format = infer_vcf_ext(cand_sv_vcf)
        shell(
            "bcftools view --threads {snakemake.threads} {bed} --output-file {cand_sv_vcf:q} --output-type {cand_sv_vcf_format} {cand_sv_vcf_path:q}"
        )

        cand_sv_idx = snakemake.output.get("cand_sv_idx", "")
        cand_sv_idx_path = results_base / "candidateSV.vcf.gz.tbi"
        if cand_sv_idx and cand_sv_idx != cand_sv_idx_path:
            shell(
                "bcftools index --threads {snakemake.threads} --output-file {cand_sv_idx:q} {cand_sv_vcf:q}"
            )
