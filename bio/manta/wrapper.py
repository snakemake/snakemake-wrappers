__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"


import math
from snakemake.shell import shell
from pathlib import Path


extra_cfg = snakemake.params.get("extra_cfg", "")
extra_run = snakemake.params.get("extra_run", "")

bams = list(map("--normalBam {}".format, snakemake.input.samples))

bed = snakemake.output.get("bed", "")
if bed:
    bed = f"--callRegions {bed}"

mem_gb = math.ceil(snakemake.resources.get("mem_mb", "") / 1024)
if not mem_gb:
    mem_gb = snakemake.resources.get("mem_gb", "")
if mem_gb:
    mem_gb = f"--memGb {mem_gb}"

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    # Configure Manta
    "configManta.py {extra_cfg} {bams} --referenceFasta {snakemake.input.ref} {bed} --runDir {snakemake.output.outdir} {log}; "
    # Run Manta
    "python2 {snakemake.output.outdir}/runWorkflow.py {extra_run} --jobs {snakemake.threads} {mem_gb} {log}; "
)


# Copy outputs into proper position.
results_base = Path(snakemake.output.outdir) / "results" / "variants"

vcf = snakemake.output.get("vcf", "")
vcf_path = results_base / "diploidSV.vcf.gz"
if vcf and vcf != vcf_path:
    shell("cp {vcf_path:q} {vcf:q}")

tbi = snakemake.output.get("tbi", "")
tbi_path = results_base / "diploidSV.vcf.gz.tbi"
if tbi and tbi != tbi_path:
    shell("cp {tbi_path:q} {tbi:q}")

cand_indel_vcf = snakemake.output.get("cand_indel_vcf", "")
cand_indel_vcf_path = results_base / "candidateSmallIndels.vcf.gz"
if cand_indel_vcf and cand_indel_vcf != cand_indel_vcf_path:
    shell("cp {cand_indel_vcf_path:q} {cand_indel_vcf:q}")

cand_indel_tbi = snakemake.output.get("cand_indel_tbi", "")
cand_indel_tbi_path = results_base / "candidateSmallIndels.vcf.gz.tbi"
if cand_indel_tbi and cand_indel_tbi != cand_indel_tbi_path:
    shell("cp {cand_indel_tbi_path:q} {cand_indel_tbi:q}")

cand_sv_vcf = snakemake.output.get("cand_sv_vcf", "")
cand_sv_vcf_path = results_base / "candidateSV.vcf.gz"
if cand_sv_vcf and cand_sv_vcf != cand_sv_vcf_path:
    shell("cp {cand_sv_vcf_path:q} {cand_sv_vcf:q}")

cand_sv_tbi = snakemake.output.get("cand_sv_tbi", "")
cand_sv_tbi_path = results_base / "candidateSV.vcf.gz.tbi"
if cand_sv_tbi and cand_sv_tbi != cand_sv_tbi_path:
    shell("cp {cand_sv_tbi_path:q} {cand_sv_tbi:q}")
