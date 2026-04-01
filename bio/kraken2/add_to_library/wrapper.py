__author__ = "Alessandro Leone"
__copyright__ = "Copyright 2026, Alessandro Leone"
__email__ = "alessandro.leone@unito.it"
__license__ = "MIT"

from snakemake.shell import shell

fasta = snakemake.input.get("fasta")
assert fasta is not None, "Input -> fasta is a required input parameter"

fasta = [fasta] if isinstance(fasta, str) else list(fasta)
fasta_str = " ".join(fasta)

extra = snakemake.params.get("extra", "")

log = snakemake.log[0] if snakemake.log else None
if log:
    log = f"--log {log}"
else:
    log = ""
    
shell(
    "k2 add-to-library"
    " --db {snakemake.input.db}"
    " --file {fasta_str}"
    " --threads {snakemake.threads}"
    " {extra}"
    " {log}"
)
