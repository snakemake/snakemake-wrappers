__author__ = "Alessandro Leone"
__copyright__ = "Copyright 2026, Alessandro Leone"
__email__ = "alessandro.leone@unito.it"
__license__ = "MIT"

import os
from pathlib import Path
from tempfile import TemporaryDirectory
from snakemake.shell import shell


extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

hash_file = snakemake.input.get("hash")
opts_file = snakemake.input.get("opts")
taxo_file = snakemake.input.get("taxo")
assert (
    hash_file and opts_file and taxo_file
), "Input -> hash, opts, and taxo are required input parameters"
db_files = [hash_file, opts_file, taxo_file]
db_dirs = [os.path.dirname(os.path.abspath(f)) for f in db_files]
assert all(
    d == db_dirs[0] for d in db_dirs
), f"All db files (hash, opts, taxo) must be in the same directory, got: {db_dirs}"
db = db_dirs[0]
fq1 = snakemake.input.get("fq1")
assert fq1 is not None, "Input -> fq1 is a required input parameter"

fq2 = snakemake.input.get("fq2")

db = [db] if isinstance(db, str) else db
fq1 = [fq1] if isinstance(fq1, str) else fq1

paired = fq2 is not None
if paired:
    fq2 = [fq2] if isinstance(fq2, str) else list(fq2)
    assert len(fq1) == len(
        fq2
    ), "Input -> equal number of files required for fq1 and fq2"

input_str_db = ",".join(db)
input_str_fq1 = " ".join(fq1)
input_str_fq2 = " ".join(fq2) if paired else ""


def format_out_flag(out_param, flag_name):
    if not out_param:
        return ""

    out_file = out_param[0] if isinstance(out_param, list) else out_param

    if paired:
        stem, ext = os.path.splitext(out_file)
        if not stem.endswith("_1"):
            raise ValueError(
                f"For paired-end data, '{flag_name}' first file must end with '_1' before the extension."
            )
        kraken_template = stem[:-2] + "#" + ext
        return f"{flag_name} {kraken_template}"
    else:
        return f"{flag_name} {out_file}"


report = snakemake.output.get("report", "")
if report:
    report = f"--report {report}"

output = snakemake.output.get("classif", "-")
if output:
    output = f"--output {output}"

classified = snakemake.output.get("classified_out", "")
if classified:
    classified = format_out_flag(classified, "--classified-out")

unclassified = snakemake.output.get("unclassified_out", "")
if unclassified:
    unclassified = format_out_flag(unclassified, "--unclassified-out")

paired_flag = "--paired" if paired else ""

shell(
    "k2 classify "
    "--db {input_str_db} "
    "--threads {snakemake.threads} "
    "{paired_flag} "
    "{report} "
    "{output} "
    "{classified} "
    "{unclassified} "
    "{extra} "
    "{input_str_fq1} {input_str_fq2} "
    "{log}"
)
