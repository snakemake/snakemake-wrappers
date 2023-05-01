__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

bed = snakemake.input.get("bed", "")
if bed:
    bed = f"--bed {bed}"

gtf = snakemake.input.get("gtf", "")
if gtf:
    gtf = f"--gtf {gtf}"


shell(
    "seqkit subseq"
    " --threads {snakemake.threads}"
    " {bed}"
    " {gtf}"
    " {extra}"
    " --out-file {snakemake.output.fasta}"
    " {snakemake.input.fasta}"
    " {log}"
)
