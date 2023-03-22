__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2021, Filipe G. Vieira"
__license__ = "MIT"

from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
if snakemake.log:
    log = f"--log {snakemake.log}"


fasta_arg = snakemake.params.get("fasta_arg", "")
if fasta_arg:
    fasta_arg = f"{fasta_arg} {snakemake.input.fasta}"


fastq_arg = snakemake.params.get("fastq_arg", "")
if fastq_arg:
    fastq_arg = f"{fastq_arg} {snakemake.input.fastq}"


db = snakemake.input.get("db", "")
if db:
    db = f"--db {db}"


out_list = list()
for key, value in snakemake.output.items():
    if value.endswith(".gz"):
        out_list.append(f"--{key} /dev/stdout | gzip > {value}")
    elif value.endswith(".bz2"):
        out_list.append(f"--{key} /dev/stdout | bzip2 > {value}")
    else:
        out_list.append(f"--{key} {value}")
 
# Check which output files are to be compressed
out_gz = [out.endswith(".gz") for out in out_list]
out_bz2 = [out.endswith(".bz2") for out in out_list]
assert sum(out_gz + out_bz2) <= 1, "only one output can be compressed"

# Move compressed file (if any) to last
output = [out for _, out in sorted(zip(out_gz or out_bz2, out_list))]


shell(
    "vsearch --threads {snakemake.threads}"
    " {fasta_arg}"
    " {fastq_arg}"
    " {db}"
    " {extra}"
    " {log}"
    " {output}"
)
