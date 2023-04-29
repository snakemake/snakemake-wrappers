__author__ = "Connor McEntee"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")

bed = snakemake.input.get("bed", None)
gtf = snakemake.input.get("gtf", None)

bed_flag = "--bed %s" % bed if bed else ""
gtf_flag = "--gtf %s" % gtf if gtf else ""

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell(
    "seqkit subseq"
    " --threads {snakemake.threads}"
    " {bed_flag}"
    " {gtf_flag}"
    " {extra}"
    " --out-file {snakemake.output.fasta}"
    " {snakemake.input.fasta}"
    " {log}"
)
