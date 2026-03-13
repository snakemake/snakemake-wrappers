__author__ = "Alessandro Leone"
__copyright__ = "Copyright 2026, Alessandro Leone"
__email__ = "alessandro.leone@unito.it"
__license__ = "MIT"

from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

db = snakemake.input.get("db")
assert db is not None, "Input -> db is a required input parameter"

fq1 = snakemake.input.get("fq1")
assert fq1 is not None, "Input -> fq1 is a required input parameter"

fq2 = snakemake.input.get("fq2")

db = [db] if isinstance(db, str) else list(db)
fq1 = [fq1] if isinstance(fq1, str) else list(fq1)

paired = fq2 is not None
if paired:
    fq2 = [fq2] if isinstance(fq2, str) else list(fq2)
    assert len(fq1) == len(
        fq2
    ), "Input -> equal number of files required for fq1 and fq2"

assert len(db) == 1, "Input -> db must contain exactly one database path"

input_str_fq1 = " ".join(fq1)
input_str_fq2 = " ".join(fq2) if paired else ""
input_str_db = db[0]

report = snakemake.output.get("report")
output = snakemake.output.get("output")


paired_flag = "--paired" if paired else ""
report_flag = f"--report {report}" if report else ""
output_flag = f"--output {output}"

shell(
    "k2 classify "
    "--db {input_str_db} "
    "--threads {snakemake.threads} "
    "{paired_flag} "
    "{report_flag} "
    "{output_flag} "
    "{extra} "
    "{input_str_fq1} {input_str_fq2} "
    "{log}"
)