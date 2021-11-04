__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"


from snakemake.shell import shell
import math

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
