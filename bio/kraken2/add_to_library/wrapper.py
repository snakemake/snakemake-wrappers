__author__ = "Alessandro Leone"
__copyright__ = "Copyright 2026, Alessandro Leone"
__email__ = "alessandro.leone@unito.it"
__license__ = "MIT"

from snakemake.shell import shell

db = snakemake.input.get("db")
assert db is not None, "Input -> db is a required input parameter"

fasta = snakemake.input.get("fasta")
assert fasta is not None, "Input -> fasta is a required input parameter"

fasta = [fasta] if isinstance(fasta, str) else list(fasta)
fasta_str = " ".join(fasta)

extra = snakemake.params.get("extra", "")

log_file = snakemake.log[0] if snakemake.log else None
log_flag = f"--log {log_file}" if log_file else ""

shell(
    "k2 add-to-library "
    "--db {db} "
    "--file {fasta_str} "
    "--threads {snakemake.threads} "
    "{log_flag} "
    "{extra}"
)
