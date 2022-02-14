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
    bed = f"--callRegions {bed}"


mem_gb = snakemake.resources.get("mem_gb", "")
if not mem_gb:
    # 20 Gb of mem by default
    mem_gb = math.ceil(snakemake.resources.get("mem_mb", 20480) / 1024)

log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)


with TemporaryDirectory() as tempdir:
    tempdir = Path(tempdir)
    run_dir = tempdir / "runDir"
    bams = []

    # Symlink BAM/CRAM files to avoid problems with filenames
    for aln, idx in zip(snakemake.input.samples, snakemake.input.index):
        aln = Path(aln)
        idx = Path(idx)
        (tempdir / aln.name).symlink_to(aln.resolve())
        bams.append(tempdir / aln.name)

        if idx.name.endswith(".bam.bai") or idx.name.endswith(".cram.crai"):
            (tempdir / idx.name).symlink_to(idx.resolve())
        if idx.name.endswith(".bai"):
            (tempdir / idx.name).with_suffix(".bam.bai").symlink_to(idx.resolve())
        elif idx.name.endswith(".crai"):
            (tempdir / idx.name).with_suffix(".cram.crai").symlink_to(idx.resolve())
        else:
            raise ValueError(f"invalid index file name provided: {idx}")

    bams = list(map("--normalBam {}".format, bams))

    shell(
        # Configure Manta
        "configManta.py {extra_cfg} {bams} --referenceFasta {snakemake.input.ref} {bed} --runDir {run_dir} {log}; "
        # Run Manta
        "python2 {run_dir}/runWorkflow.py {extra_run} --jobs {snakemake.threads} --memGb {mem_gb} {log}; "
    )

    # Copy outputs into proper position.
    def infer_vcf_ext(vcf):
        if vcf.endswith(".vcf.gz"):
            return "z"
        elif vcf.endswith(".bcf"):
            return "b"
        else:
            raise ValueError(
                "invalid VCF extension. Only '.vcf.gz' and '.bcf' are supported."
            )

    def copy_vcf(origin_vcf, dest_vcf, dest_idx):
        if dest_vcf and dest_vcf != origin_vcf:
            dest_vcf_format = infer_vcf_ext(dest_vcf)
            shell(
                "bcftools view --threads {snakemake.threads} --output {dest_vcf:q} --output-type {dest_vcf_format} {origin_vcf:q} {log}"
            )

            origin_idx = str(origin_vcf) + ".tbi"
            if dest_idx and dest_idx != origin_idx:
                shell(
                    "bcftools index --threads {snakemake.threads} --output {dest_idx:q} {dest_vcf:q} {log}"
                )

    results_base = run_dir / "results" / "variants"

    # Copy main VCF output
    vcf_temp = results_base / "diploidSV.vcf.gz"
    vcf_final = snakemake.output.get("vcf")
    idx_final = snakemake.output.get("idx")
    copy_vcf(vcf_temp, vcf_final, idx_final)

    # Copy candidate small indels VCF
    cand_indel_vcf_temp = results_base / "candidateSmallIndels.vcf.gz"
    cand_indel_vcf_final = snakemake.output.get("cand_indel_vcf")
    cand_indel_idx_final = snakemake.output.get("cand_indel_idx")
    copy_vcf(cand_indel_vcf_temp, cand_indel_vcf_final, cand_indel_idx_final)

    # Copy candidates structural variants VCF
    cand_sv_vcf_temp = results_base / "candidateSV.vcf.gz"
    cand_sv_vcf_final = snakemake.output.get("cand_sv_vcf")
    cand_sv_idx_final = snakemake.output.get("cand_sv_idx")
    copy_vcf(cand_sv_vcf_temp, cand_sv_vcf_final, cand_sv_idx_final)
