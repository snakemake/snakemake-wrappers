__author__ = "Filipe G. Vieira"
__copyright__ = "Copyright 2024, Filipe G. Vieira"
__license__ = "MIT"

import os
import tempfile
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


# Input
if snakemake.input.get("tax_map"):
    extra += f" --tax-mapping-file {snakemake.input.tax_map}"
taxdump = snakemake.input.get("taxdump")


# Output
out = snakemake.output.get("db")
if isinstance(out, list):
    out = os.path.commonprefix(out)


with tempfile.TemporaryDirectory() as tmpdir:
    # Modules with threads
    if snakemake.params.module.startswith("databases "):
        input = ""
        extra += f" --threads {snakemake.threads}"
    # Modules with no temp folder
    elif snakemake.params.module == "createdb":
        input = snakemake.input.fas
        tmpdir = ""
    # Modules with no out folder
    elif snakemake.params.module == "createtaxdb":
        input = snakemake.input.db
        out = ""
    else:
        raise ValueError(
            f"The module specified under 'params' is invalid: '{snakemake.params.module}'."
        )

    # Auto-uncompress taxdump file
    if taxdump:
        if taxdump.endswith(".tar.gz"):
            import tarfile

            tar = tarfile.open(taxdump, "r:gz")
            taxdump = tmpdir / "taxdump"
            tar.extractall(taxdump)
            tar.close()
        extra += f" --ncbi-tax-dump {taxdump}"

    shell("mmseqs {snakemake.params.module} {input} {out} {tmpdir} {extra} {log}")
